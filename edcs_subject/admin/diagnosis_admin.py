from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import DiagnosisCrfForm
from ..models import DiagnosisCrf
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DiagnosisCrf, site=edcs_subject_admin)
class SubjectDiagnosisAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = DiagnosisCrfForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Final diagnosis",
            {
                "fields": (
                    "TB_dx",
                    "TB_dx_made",
                    "TB_dx_made_other",
                    "TB_dx_xpert_truenat_nga",
                    "TB_dx_xpert_truenat_nga_date",
                    "TB_dx_other_tests",
                    "info_TB_dx_made",
                    "info_TB_dx_made_other",
                ),
            },
        ),
        (
            "TB treatment",
            {
                "fields": (
                    "TB_treatment_start",
                    "TB_treatment_start_date",
                    "health_facility",
                    "reason_not_started",
                    "treatment_regimen",
                    "treatment_regimen_other",
                    "treatment_based_result",
                    "treatment_based_result_other",
                    "regimen_changed",
                    "regimen_changed_no",
                    "regimen_change1_date",
                    "regimen_change1",
                    "regimen_change1_reasons",
                    "regimen_change2_date",
                    "regimen_change2",
                    "regimen_change2_reasons",
                    "regimen_change3_date",
                    "regimen_change3",
                    "regimen_change3_reasons",
                    "treatment_outcome",
                ),
            },
        ),
        (
            "Diagnosis other than TB",
            {
                "fields": (
                    "other_dx",
                    "other_dx_pneumonia",
                    "other_dx_other",
                    "other_disease",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "TB_dx",
        "TB_dx_made",
        "TB_dx_xpert_truenat_nga",
        "TB_treatment_start",
        "created",
    )

    list_filter = (
        "report_datetime",
    )

    search_fields = ("report_datetime",)

    filter_horizontal = [
        "info_TB_dx_made",
        "other_dx",
    ]

    radio_fields = {
        "TB_dx": admin.VERTICAL,
        "TB_dx_made": admin.VERTICAL,
        "TB_dx_xpert_truenat_nga": admin.VERTICAL,
        "TB_treatment_start": admin.VERTICAL,
        "treatment_regimen": admin.VERTICAL,
        "treatment_based_result": admin.VERTICAL,
        "regimen_changed": admin.VERTICAL,
        "treatment_outcome": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
