from django.core.management.base import BaseCommand

from api.models import Post, Profile
from api.utils.media import build_media_url


class Command(BaseCommand):
    help = "Verify database image fields and print resolved media URLs."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Profile images"))
        profiles = Profile.objects.select_related("user").all()
        for profile in profiles[:20]:
            url = build_media_url(None, profile.image) if profile.image else None
            self.stdout.write(
                f"  [{profile.id}] {profile.user.email} -> {profile.image.name if profile.image else 'NO IMAGE'} | {url}"
            )
        if profiles.count() > 20:
            self.stdout.write(f"  ... and {profiles.count() - 20} more profiles")

        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING("Active post images"))
        posts = Post.objects.filter(status="Active").select_related("user")
        with_image = posts.exclude(image="").exclude(image__isnull=True)
        self.stdout.write(f"  Active posts: {posts.count()}")
        self.stdout.write(f"  With image file: {with_image.count()}")

        for post in with_image[:15]:
            url = build_media_url(None, post.image)
            self.stdout.write(f"  [{post.id}] {post.title[:50]} -> {url}")

        if with_image.count() > 15:
            self.stdout.write(f"  ... and {with_image.count() - 15} more posts")

        missing = posts.filter(image="") | posts.filter(image__isnull=True)
        if missing.exists():
            self.stdout.write(self.style.WARNING(f"\n  Posts missing images: {missing.count()}"))
