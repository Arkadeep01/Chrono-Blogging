"""
Create demo users, categories, and blog posts for Curious Chronicle.

Usage (from backend/):
    python manage.py seed_blog
    python manage.py seed_blog --clear
"""

from datetime import timedelta
import random

from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from api.models import Category, Post, Profile, User

from generator.data import (
    DEFAULT_SEED_PASSWORD,
    SEED_CATEGORIES,
    SEED_EMAIL_DOMAIN,
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
        profile.save()

        users[item["email"]] = user
    return users


def _spread_post_dates(posts_created):
    """Stagger publish dates so the homepage feels lived-in."""
    now = timezone.now()
    for index, post in enumerate(posts_created):
        days_ago = random.randint(1, 90) + index % 7
        post.date = now - timedelta(days=days_ago, hours=random.randint(0, 12))
        post.save(update_fields=["date"])


def _create_posts(users, categories, stdout=None):
    created_posts = []
    skipped = 0

    for entry in SEED_POSTS:
        user = users.get(entry["author_email"])
        category = categories.get(entry["category_slug"])
        if not user or not category:
            _write(
                stdout,
                f"Skipping post (missing user/category): {entry['title']}",
            )
            skipped += 1
            continue

        profile = Profile.objects.get(user=user)
        exists = Post.objects.filter(user=user, title=entry["title"]).exists()
        if exists:
            skipped += 1
            continue

        post = Post.objects.create(
            user=user,
            profile=profile,
            category=category,
            title=entry["title"],
            description=entry["description"],
            tags=entry["tags"],
            status="Active",
            views=entry.get("views", 0),
            slug=slugify(entry["title"]),
        )
        created_posts.append(post)

    _spread_post_dates(created_posts)
    return created_posts, skipped


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
    users = _ensure_users(password)
    created_posts, skipped = _create_posts(users, categories, stdout=stdout)

    summary = {
        "users": len(users),
        "categories": len(categories),
        "posts_created": len(created_posts),
        "posts_skipped": skipped,
        "password": password,
        "email_domain": SEED_EMAIL_DOMAIN,
    }

    _write(stdout, "")
    _write(stdout, "Seed complete:")
    _write(stdout, f"  Demo users: {summary['users']}")
    _write(stdout, f"  Categories: {summary['categories']}")
    _write(stdout, f"  Posts created: {summary['posts_created']}")
    _write(stdout, f"  Posts skipped (already exist): {summary['posts_skipped']}")
    _write(stdout, f"  Login password for all demo accounts: {password}")
    _write(stdout, "")
    _write(stdout, "Demo accounts (email is the login):")
    for item in SEED_USERS:
        _write(stdout, f"  - {item['email']} ({item['full_name']})")

    return summary
