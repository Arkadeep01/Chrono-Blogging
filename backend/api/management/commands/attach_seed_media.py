from django.core.management.base import BaseCommand, CommandError

from api.models import User
from generator.attach_media import attach_seed_media
from generator.data import SEED_EMAIL_DOMAIN, SEED_USERS


class Command(BaseCommand):
    help = (
        "Attach images from media/seed/avatars and media/seed/posts "
        "to demo users and blog posts (run seed_blog first)."
    )

    def handle(self, *args, **options):
        demo_users = User.objects.filter(email__iendswith=f"@{SEED_EMAIL_DOMAIN}").count()
        if demo_users == 0:
            raise CommandError(
                "No demo users found. Run first:\n  python manage.py seed_blog"
            )

        self.stdout.write(self.style.MIGRATE_HEADING("Attaching seed media..."))
        self.stdout.write("")
        self.stdout.write("Expected folders: media/seed/avatar/ and media/seed/post/")
        self.stdout.write("  Avatars: {username}.jpg (see SEED_USERS)")
        self.stdout.write("  Posts: filenames in generator/data.py (SEED_POST_IMAGE_FILES)")
        self.stdout.write("")

        try:
            result = attach_seed_media(stdout=self.stdout)
        except FileNotFoundError as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Avatars attached: {result['avatars_attached']}/{result['avatars_expected']}"
        ))
        self.stdout.write(self.style.SUCCESS(
            f"Post images attached: {result['posts_attached']}/{result['posts_expected']}"
        ))

        if result["avatars_missing"]:
            self.stdout.write(self.style.WARNING(
                "Missing avatars: " + ", ".join(result["avatars_missing"])
            ))
        if result["posts_missing"]:
            self.stdout.write(self.style.WARNING(
                f"Missing post images: {len(result['posts_missing'])} files"
            ))
            for line in result["posts_missing"][:5]:
                self.stdout.write(f"    {line}")
            if len(result["posts_missing"]) > 5:
                self.stdout.write(f"    ... and {len(result['posts_missing']) - 5} more")

        self.stdout.write("")
        self.stdout.write("Verify URLs with:")
        self.stdout.write("  python manage.py check_media")
