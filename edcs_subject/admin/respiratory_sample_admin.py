from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
# from ..forms import ClinicalReviewForm
from ..models import RespiratorySample
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(RespiratorySample, site=edcs_subject_admin)
class SubjectRespiratorySampleAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    # form = ClinicalReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Respiratory sample",
            {
                "fields": (
                    "respiratory_sample",
                    "respiratory_sample_yes",
                    "respiratory_sample_no",
                    "respiratory_sample_no_other",
                    "respiratory_sample1_date",
                    "respiratory_sample2_date",
                    "respiratory_sample3_date",
                    "sample_lab_receive_date",
                    "sputum_respiratory_sample",
                    "nga_respiratory_sample",
                    "appearance",
                    "sample_volume",
                    "accession_status",
                    "afb_microscopy_date_a",
                    "afb_technique_a",
                    "afb_result_a",
                    "afb_microscopy_date_b",
                    "afb_technique_b",
                    "afb_result_b",
                    "xpert_mtb_date",
                    "xpert_mtb",
                    "mtb_error_code",
                    "rif_resistance",
                    "spc_ct_available",
                    "spc_ct_value",
                    "test_repeated",
                    "test_repeated_date",
                    "test_not_repeated_reason",
                    "test_not_repeated_reason_other",
                    "repeat_xpert_mtb_date",
                    "repeat_xpert_mtb",
                    "repeat_mtb_error_code",
                    "repeat_rif_resistance",
                    "repeat_spc_ct_available",
                    "repeat_spc_ct_value",
                    "truenat_mtb_plus_date",
                    "truenat_plus_mtb",
                    "truenat_plus_error_code",
                    "truenat_rif_resistance",
                    "truenat_spc_ct_available",
                    "truenat_spc_ct_value",
                    "truenat_test_repeated",
                    "truenat_test_repeated_date",
                    "truenat_test_not_repeated_reason",
                    "truenat_test_not_repeated_reason_other",
                    "truenat_repeat_xpert_mtb_date",
                    "truenat_repeat_xpert_mtb",
                    "truenat_repeat_mtb_error_code",
                    "truenat_repeat_rif_resistance",
                    "truenat_repeat_spc_ct_available",
                    "truenat_repeat_spc_ct_value",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "respiratory_sample",
        "respiratory_sample_yes",
        "respiratory_sample_no",
        "appearance",
        "created",
    )

    list_filter = (
        "report_datetime",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "respiratory_sample": admin.VERTICAL,
        "respiratory_sample_yes": admin.VERTICAL,
        "respiratory_sample_no": admin.VERTICAL,
        "appearance": admin.VERTICAL,
        "accession_status": admin.VERTICAL,
        "afb_technique_a": admin.VERTICAL,
        "afb_result_a": admin.VERTICAL,
        "afb_technique_b": admin.VERTICAL,
        "afb_result_b": admin.VERTICAL,
        "xpert_mtb": admin.VERTICAL,
        "mtb_error_code": admin.VERTICAL,
        "rif_resistance": admin.VERTICAL,
        "spc_ct_available": admin.VERTICAL,
        "test_repeated": admin.VERTICAL,
        "test_not_repeated_reason": admin.VERTICAL,
        "repeat_xpert_mtb": admin.VERTICAL,
        "repeat_mtb_error_code": admin.VERTICAL,
        "repeat_rif_resistance": admin.VERTICAL,
        "repeat_spc_ct_available": admin.VERTICAL,
        "truenat_plus_mtb": admin.VERTICAL,
        "truenat_plus_error_code": admin.VERTICAL,
        "truenat_rif_resistance": admin.VERTICAL,
        "truenat_spc_ct_available": admin.VERTICAL,
        "truenat_test_repeated": admin.VERTICAL,
        "truenat_test_not_repeated_reason": admin.VERTICAL,
        "truenat_repeat_xpert_mtb": admin.VERTICAL,
        "truenat_repeat_mtb_error_code": admin.VERTICAL,
        "truenat_repeat_rif_resistance": admin.VERTICAL,
        "truenat_repeat_spc_ct_available": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
