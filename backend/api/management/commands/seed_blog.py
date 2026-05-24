from django.core.management.base import BaseCommand

from generator.data import DEFAULT_SEED_PASSWORD
from generator.seed_blog import run_seed


class Command(BaseCommand):
    help = "Seed 5 demo user accounts and 30 blog posts across categories."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing demo users (@demo.curiouschronicle.app) before seeding.",
        )
        parser.add_argument(
            "--password",
            default=DEFAULT_SEED_PASSWORD,
            help=f"Password for demo accounts (default: {DEFAULT_SEED_PASSWORD}).",
        )

    def handle(self, *args, **options):
        run_seed(
            clear=options["clear"],
            password=options["password"],
            stdout=self.stdout,
        )
