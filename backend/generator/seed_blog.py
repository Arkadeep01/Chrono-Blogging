"""
Create demo users, categories, and blog posts for Curious Chronicle.

Usage (from backend/):
    python manage.py seed_blog
    python manage.py seed_blog --clear
"""

from datetime import timedelta
import random
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from api.models import Category, Post, Profile, User

from generator.data import (
    DEFAULT_SEED_PASSWORD,
    SEED_CATEGORIES,
    SEED_EMAIL_DOMAIN,
    SEED_POST_IMAGE_FILES,
    SEED_POSTS,
    SEED_USERS,
)


def _write(stdout, message, style=None):
    if stdout is None:
        return
    if style:
        stdout.write(style(message))
    else:
        stdout.write(message)


def clear_seed_data(stdout=None):
    """Remove demo users (and their posts via CASCADE) created by this seeder."""
    deleted_users, _ = User.objects.filter(email__iendswith=f"@{SEED_EMAIL_DOMAIN}").delete()
    _write(stdout, f"Removed {deleted_users} seed-related object(s).")


def _ensure_categories():
    categories = {}
    for item in SEED_CATEGORIES:
        category, _ = Category.objects.get_or_create(
            slug=item["slug"],
            defaults={"title": item["title"]},
        )
        if category.title != item["title"]:
            category.title = item["title"]
            category.save(update_fields=["title"])
        categories[item["slug"]] = category
    return categories


def _ensure_users(password):
    users = {}
    profile_images_assigned = 0
    for item in SEED_USERS:
        user, created = User.objects.get_or_create(
            email=item["email"],
            defaults={
                "username": item["username"],
                "full_name": item["full_name"],
            },
        )
        if created:
            user.set_password(password)
            user.save()
        else:
            updated = False
            if user.username != item["username"]:
                user.username = item["username"]
                updated = True
            if user.full_name != item["full_name"]:
                user.full_name = item["full_name"]
                updated = True
            if updated:
                user.save()

        profile, _ = Profile.objects.get_or_create(user=user)
        profile_data = item["profile"]
        profile.full_name = item["full_name"]
        profile.bio = profile_data.get("bio")
        profile.country = profile_data.get("country")
        profile.author = profile_data.get("author", True)
        if _assign_profile_avatar(profile, item["email"]):
            profile_images_assigned += 1
        profile.save()

        users[item["email"]] = user
    return users, profile_images_assigned


def _spread_post_dates(posts_created):
    """Stagger publish dates so the homepage feels lived-in."""
    now = timezone.now()
    for index, post in enumerate(posts_created):
        days_ago = random.randint(1, 90) + index % 7
        post.date = now - timedelta(days=days_ago, hours=random.randint(0, 12))
        post.save(update_fields=["date"])


def _assign_profile_avatar(profile, user_email):
    username = user_email.split("@")[0].replace(".", "_")
    avatar_path = Path(settings.MEDIA_ROOT) / "seed" / "avatar" / f"{username}.jpg"
    if not avatar_path.exists():
        avatar_path = Path(settings.MEDIA_ROOT) / "seed" / "avatar" / "avatar.png"
        if not avatar_path.exists():
            return False

    with avatar_path.open("rb") as image_file:
        profile.image.save(f"seed/avatar/{avatar_path.name}", File(image_file), save=False)
    return True


def _assign_post_image(post, image_file_name):
    if not image_file_name:
        return False

    image_path = Path(settings.MEDIA_ROOT) / "seed" / "post" / image_file_name
    if not image_path.exists():
        return False

    with image_path.open("rb") as image_file:
        post.image.save(f"seed/post/{image_file_name}", File(image_file), save=False)
    return True


def _create_posts(users, categories, stdout=None):
    created_posts = []
    updated_posts = 0
    post_images_assigned = 0
    skipped = 0

    for index, entry in enumerate(SEED_POSTS):
        user = users.get(entry["author_email"])
        category = categories.get(entry["category_slug"])
        image_name = SEED_POST_IMAGE_FILES[index] if index < len(SEED_POST_IMAGE_FILES) else None
        if not user or not category:
            _write(
                stdout,
                f"Skipping post (missing user/category): {entry['title']}",
            )
            skipped += 1
            continue

        profile = Profile.objects.get(user=user)
        post, created = Post.objects.get_or_create(
            user=user,
            title=entry["title"],
            defaults={
                "profile": profile,
                "category": category,
                "description": entry["description"],
                "tags": entry["tags"],
                "status": "Active",
                "views": entry.get("views", 0),
                "slug": slugify(entry["title"]),
            },
        )

        if created:
            created_posts.append(post)
        else:
            post.profile = profile
            post.category = category
            post.description = entry["description"]
            post.tags = entry["tags"]
            post.status = "Active"
            post.views = entry.get("views", 0)
            if not post.slug:
                post.slug = slugify(entry["title"])
            updated_posts += 1

        if _assign_post_image(post, image_name):
            post_images_assigned += 1

        post.save()

    _spread_post_dates(created_posts)
    return created_posts, updated_posts, skipped, post_images_assigned


@transaction.atomic
def run_seed(clear=False, password=None, stdout=None):
    """
    Seed 5 demo accounts and up to 30 Active blog posts.

    Returns a dict summary for tests or programmatic use.
    """
    password = password or DEFAULT_SEED_PASSWORD

    if clear:
        clear_seed_data(stdout=stdout)

    categories = _ensure_categories()
    users, profile_images_assigned = _ensure_users(password)
    created_posts, updated_posts, skipped, post_images_assigned = _create_posts(
        users, categories, stdout=stdout
    )

    summary = {
        "users": len(users),
        "categories": len(categories),
        "posts_created": len(created_posts),
        "posts_updated": updated_posts,
        "posts_skipped": skipped,
        "profile_images_assigned": profile_images_assigned,
        "post_images_assigned": post_images_assigned,
        "password": password,
        "email_domain": SEED_EMAIL_DOMAIN,
    }

    _write(stdout, "")
    _write(stdout, "Seed complete:")
    _write(stdout, f"  Demo users: {summary['users']}")
    _write(stdout, f"  Categories: {summary['categories']}")
    _write(stdout, f"  Posts created: {summary['posts_created']}")
    _write(stdout, f"  Posts updated: {summary['posts_updated']}")
    _write(stdout, f"  Posts skipped (missing deps): {summary['posts_skipped']}")
    _write(stdout, f"  Profile images assigned: {summary['profile_images_assigned']}")
    _write(stdout, f"  Post images assigned: {summary['post_images_assigned']}")
    _write(stdout, f"  Login password for all demo accounts: {password}")
    _write(stdout, "")
    _write(stdout, "Demo accounts (email is the login):")
    for item in SEED_USERS:
        _write(stdout, f"  - {item['email']} ({item['full_name']})")

    return summary
