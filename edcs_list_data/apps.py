import sys

from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from django.db.models.signals import post_migrate

from .site_list_data import SiteListDataError, site_list_data

style = color_style()


"""
If you need list data in your tests add to your test case:

    @classmethod
    def setUpClass(cls):
        site_list_data.autodiscover()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

"""


def post_migrate_list_data(sender=None, **kwargs):

    sys.stdout.write(style.MIGRATE_HEADING("Updating list data:\n"))

    site_list_data.autodiscover()
    site_list_data.load_data()
    sys.stdout.write("Done.\n")
    sys.stdout.flush()


class AppConfig(DjangoAppConfig):
    name = "edcs_list_data"
    verbose_name = "Edcs List Data"

    def ready(self):
        post_migrate.connect(post_migrate_list_data, sender=self)
