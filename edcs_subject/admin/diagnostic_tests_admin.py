from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import ClinicalReviewForm
from ..models import DiagnosticTests
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DiagnosticTests, site=edcs_subject_admin)
class SubjectDiagnosticTestsAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    # form = ClinicalReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Reason(s) for being regarded a presumptive TB patient at initial assessment",
            {
                "fields": (
                    "sample_type_a",
                    "xpert_mtb_rif_a",
                    "truenat_mtb_plus_a",
                    "culture_a",
                    "smear_microscopy_a",
                    "mods_a",
                    "other_test_a",
                    "other_test_result_a",
                    "sample_type_b",
                    "xpert_mtb_rif_b",
                    "truenat_mtb_plus_b",
                    "culture_b",
                    "smear_microscopy_b",
                    "mods_b",
                    "other_test_b",
                    "other_test_result_b",
                    "remarks",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "xpert_mtb_rif_a",
        "truenat_mtb_plus_a",
        "culture_a",
        "smear_microscopy_a",
        "created",
    )

    list_filter = (
        "report_datetime",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "sample_type_a": admin.VERTICAL,
        "xpert_mtb_rif_a": admin.VERTICAL,
        "truenat_mtb_plus_a": admin.VERTICAL,
        "culture_a": admin.VERTICAL,
        "smear_microscopy_a": admin.VERTICAL,
        "mods_a": admin.VERTICAL,
        "other_test_a": admin.VERTICAL,
        "other_test_result_a": admin.VERTICAL,
        "xpert_mtb_rif_b": admin.VERTICAL,
        "truenat_mtb_plus_b": admin.VERTICAL,
        "culture_b": admin.VERTICAL,
        "smear_microscopy_b": admin.VERTICAL,
        "mods_b": admin.VERTICAL,
        "other_test_b": admin.VERTICAL,
        "other_test_result_b": admin.VERTICAL,
        "remarks": admin.VERTICAL,
    }
