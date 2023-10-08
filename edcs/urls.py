from django.contrib import admin
from django.urls import include, path

from edcs_dashboard.views import AdministrationView
from edcs_utils.paths_for_urlpatterns import paths_for_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", include("edcs_dashboard.urls")),
    path("administration/", AdministrationView.as_view(), name="administration_url"),
    *paths_for_urlpatterns("edcs_device"),
    *paths_for_urlpatterns("edcs_notification"),
    *paths_for_urlpatterns("edcs_appointment"),
    *paths_for_urlpatterns("edcs_crf"),
    *paths_for_urlpatterns("edcs_export"),
    *paths_for_urlpatterns("edcs_facility"),
    *paths_for_urlpatterns("edcs_identifier"),
    *paths_for_urlpatterns("edcs_lists"),
    *paths_for_urlpatterns("edcs_screening"),
    *paths_for_urlpatterns("edcs_subject"),
    *paths_for_urlpatterns("edcs_consent"),
    *paths_for_urlpatterns("edcs_registration"),
    *paths_for_urlpatterns("edcs_visit_schedule"),
    # path("defender/", include("defender.urls")),
    path("", include("edcs_auth.urls")),
]
