from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import EnrollmentCrfForm
from ..models import EnrollmentCRF
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(EnrollmentCRF, site=edcs_subject_admin)
class SubjectEnrollmentAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = EnrollmentCrfForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Reason(s) for being regarded a presumptive TB patient at initial assessment",
            {
                "fields": (
                    "cough",
                    "weight_gain_loss",
                    "cough_blood",
                    "fever",
                    "night_sweat",
                    "neck_enlarged",
                    "contact_TB_patient",
                ),
            },
        ),
        (
            "History of TB and previous treatment",
            {
                "fields": (
                    "TB_treatment",
                    "TB_treatment_duration",
                    "TB_treatment_regimen",
                    "TB_treatment_outcome",
                ),
            },
        ),
        (
            "Health-related conditions",
            {
                "fields": (
                    "hiv_status",
                    "immuno_diseases",
                    "immuno_diseases_specify",
                    "other_disease",
                    "other_disease_specify",
                    "other_disease_specify_other",
                ),
            },
        ),
        (
            "Samples collected",
            {
                "fields": (
                    "resp_sample",
                    "resp_sample_DST_date",
                    "resp_sample_type_DST",
                    "resp_sample_seq_date",
                    "resp_sample_type_seq",
                    "pleural_fluid",
                    "pleural_fluid_date",
                    "csf",
                    "csf_date",
                    "peritoneal_fluid",
                    "peritoneal_fluid_date",
                    "pericardial_fluid",
                    "pericardial_fluid_date",
                    "lymph_node_aspirate",
                    "lymph_node_aspirate_date",
                    "stool",
                    "stool_date",
                    "chest_xray",
                    "chest_xray_date",
                    "other_requested_sample",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "cough",
        "weight_gain_loss",
        "cough_blood",
        "fever",
        "created",
    )

    list_filter = (
        "report_datetime",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "cough": admin.VERTICAL,
        "weight_gain_loss": admin.VERTICAL,
        "cough_blood": admin.VERTICAL,
        "fever": admin.VERTICAL,
        "night_sweat": admin.VERTICAL,
        "neck_enlarged": admin.VERTICAL,
        "contact_TB_patient": admin.VERTICAL,
        "TB_treatment": admin.VERTICAL,
        "hiv_status": admin.VERTICAL,
        "immuno_diseases": admin.VERTICAL,
        "other_disease": admin.VERTICAL,
        "other_disease_specify": admin.VERTICAL,
        "resp_sample": admin.VERTICAL,
        "pleural_fluid": admin.VERTICAL,
        "csf": admin.VERTICAL,
        "peritoneal_fluid": admin.VERTICAL,
        "pericardial_fluid": admin.VERTICAL,
        "lymph_node_aspirate": admin.VERTICAL,
        "stool": admin.VERTICAL,
        "chest_xray": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
