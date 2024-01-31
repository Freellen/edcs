"""Default sites module.

Define ``sites.py`` in your own module and set EDCS_SITES_MODULE_NAME
to the name of that module.

"""
from django.conf import settings

from edcs_sites.single_site import SingleSite

default_country = getattr(settings, "EDCS_SITES_DEFAULT_COUNTRY", "tanzania")
default_country_code = getattr(settings, "EDCS_SITES_DEFAULT_COUNTRY_CODE", "tz")
default_domain = getattr(settings, "EDCS_SITES_DEFAULT_DOMAIN", "localhost")

fqdn = settings.EDCS_DOMAIN
edcs = ""

if settings.EDCS_SITES_LIVE_DOMAIN:
    edcs = "edcs."


# site_id, name, **kwargs
all_sites = {
    "tanzania": (
        SingleSite(
            10,
            "Central Tuberculosis Reference Laboratory (CTRL)",
            title="Central Tuberculosis Reference Laboratory",
            country_code="tz",
            country="tanzania",
            domain=f"ctrl.tz.{edcs}{fqdn}",
        ),
    ),
}
