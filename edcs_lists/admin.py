from django.contrib import admin

from edcs_list_data.admin import ListModelAdminMixin

from .admin_site import edcs_lists_admin
from .models import (
    InfoTbDxMade,
    OtherDxMade,
)


@admin.register(InfoTbDxMade, site=edcs_lists_admin)
class InfoTbDxMadeAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(OtherDxMade, site=edcs_lists_admin)
class OtherDxMadeAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
