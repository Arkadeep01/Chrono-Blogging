"""
Attach images from backend/media/seed/ to demo profiles and posts.

Supports folders:
  media/seed/avatar/ or avatars/
  media/seed/post/   or posts/

Post images: use SEED_POST_IMAGE_FILES in data.py (slug-style names),
or legacy numbered files 01.jpg … 30.jpg in posts/.
"""

from pathlib import Path

from django.conf import settings
from django.core.files import File

from api.models import Post, Profile

from generator.data import SEED_POSTS, SEED_POST_IMAGE_FILES, SEED_USERS

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")


def _resolve_seed_dir(seed_root: Path, *names: str):
    """
    Pick the seed folder that actually contains images.
    Prefer non-empty dirs so empty `posts/` does not shadow `post/`.
    """
    candidates = [seed_root / name for name in names if (seed_root / name).is_dir()]
    if not candidates:
        return None

    def has_images(directory: Path):
        return any(
            p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
            for p in directory.iterdir()
        )

    for directory in candidates:
        if has_images(directory):
            return directory

    return candidates[0]


def _find_image_file(directory: Path, stem: str):
    """Find image by stem (e.g. alexchen) trying common extensions."""
    for ext in IMAGE_EXTENSIONS:
        candidate = directory / f"{stem}{ext}"
        if candidate.is_file():
            return candidate
    return None


def _find_image_by_filename(directory: Path, filename: str):
    """Find exact filename, or same stem with another extension."""
    exact = directory / filename
    if exact.is_file():
        return exact
    stem = Path(filename).stem
    return _find_image_file(directory, stem)


def _attach_file_to_imagefield(instance, field_name: str, file_path: Path):
    field = getattr(instance, field_name)
    with file_path.open("rb") as handle:
        field.save(file_path.name, File(handle), save=True)


def attach_seed_media(stdout=None):
    seed_root = Path(settings.MEDIA_ROOT) / "seed"
    avatars_dir = _resolve_seed_dir(seed_root, "avatar", "avatars")
    posts_dir = _resolve_seed_dir(seed_root, "post", "posts")

    if not avatars_dir and not posts_dir:
        raise FileNotFoundError(
            f"Seed media folders not found under {seed_root}. "
            "Create media/seed/avatar/ and/or media/seed/post/"
        )

    avatars_attached = 0
    posts_attached = 0
    avatars_missing = []
    posts_missing = []

    if avatars_dir:
        for item in SEED_USERS:
            avatar_file = item.get("avatar_file")
            if avatar_file:
                image_path = _find_image_by_filename(avatars_dir, avatar_file)
            else:
                image_path = _find_image_file(avatars_dir, item["username"])

            if not image_path:
                avatars_missing.append(item["username"])
                continue

            try:
                profile = Profile.objects.get(user__email=item["email"])
            except Profile.DoesNotExist:
                avatars_missing.append(item["username"])
                continue

            _attach_file_to_imagefield(profile, "image", image_path)
            avatars_attached += 1
            if stdout:
                stdout.write(f"  Avatar: {item['username']} <- {image_path.name}")

    if posts_dir:
        use_named_files = len(SEED_POST_IMAGE_FILES) == len(SEED_POSTS)

        for index, entry in enumerate(SEED_POSTS, start=1):
            if use_named_files:
                image_path = _find_image_by_filename(
                    posts_dir, SEED_POST_IMAGE_FILES[index - 1]
                )
            else:
                image_path = _find_image_file(posts_dir, f"{index:02d}")

            if not image_path:
                label = (
                    SEED_POST_IMAGE_FILES[index - 1]
                    if use_named_files
                    else f"{index:02d}"
                )
                posts_missing.append(f"{label} ({entry['title'][:40]}...)")
                continue

            post = Post.objects.filter(
                user__email=entry["author_email"],
                title=entry["title"],
            ).first()

            if not post:
                posts_missing.append(f"{image_path.name} (post not in DB)")
                continue

            _attach_file_to_imagefield(post, "image", image_path)
            posts_attached += 1
            if stdout:
                stdout.write(f"  Post {index:02d}: {post.title[:50]} <- {image_path.name}")

    return {
        "avatars_attached": avatars_attached,
        "posts_attached": posts_attached,
        "avatars_missing": avatars_missing,
        "posts_missing": posts_missing,
        "avatars_expected": len(SEED_USERS),
        "posts_expected": len(SEED_POSTS),
    }
