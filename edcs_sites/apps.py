import sys

from django.apps import AppConfig as DjangoAppConfig
from django.apps import apps as django_apps
from django.core.management.color import color_style
from django.db.models.signals import post_migrate

from .get_all_sites import get_all_sites

style = color_style()


def post_migrate_update_sites(sender=None, **kwargs):
    from edcs_sites.add_or_update_django_sites import add_or_update_django_sites

    sys.stdout.write(style.MIGRATE_HEADING("Updating sites:\n"))

    for country, sites in get_all_sites().items():
        sys.stdout.write(style.MIGRATE_HEADING(f" (*) sites for {country} ...\n"))
        add_or_update_django_sites(
            apps=django_apps,
            sites=sites,
            verbose=True,
        )
    sys.stdout.write("Done.\n")
    sys.stdout.flush()


class AppConfig(DjangoAppConfig):
    name = "edcs_sites"
    has_exportable_data = True
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        post_migrate.connect(post_migrate_update_sites, sender=self)
