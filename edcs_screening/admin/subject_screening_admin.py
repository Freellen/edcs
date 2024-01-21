from django.contrib import admin, messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django_audit_fields import audit_fieldset_tuple

from edcs_model_admin import SimpleHistoryAdmin
from edcs_model_admin.dashboard import ModelAdminDashboardMixin
from edcs_screening.admin_site import edcs_screening_admin
from edcs_screening.forms.subject_screening_form import SubjectScreeningForm
from edcs_screening.models import SubjectScreening


@admin.register(SubjectScreening, site=edcs_screening_admin)
class SubjectScreeningAdmin(ModelAdminDashboardMixin, SimpleHistoryAdmin):
    form = SubjectScreeningForm
    fieldsets = (
        [
            None,
            {
                "fields": (
                    "report_datetime",
                    "patient_18yrs",
                    "symptoms_pulmonary",
                    "respiratory_sample",
                    "consent",
                    "patient_id",
                    "patient_know_dob",
                    "patient_dob",
                    "age_in_years",
                    "gender",
                    "initials",
                ),
            },
        ],
        audit_fieldset_tuple,
    )

    list_display = (
        "screening_identifier",
        "patient_18yrs",
        "gender",
        "report_datetime",
        "user_created",
        "created",
    )

    list_filter = (
        "report_datetime",
        "gender",
    )

    search_fields = ("screening_identifier",)

    radio_fields = {
        "patient_18yrs": admin.VERTICAL,
        "symptoms_pulmonary": admin.VERTICAL,
        "respiratory_sample": admin.VERTICAL,
        "consent": admin.VERTICAL,
        "patient_know_dob": admin.VERTICAL,
        "gender": admin.VERTICAL,
    }

    def response_post_save_add(self, request, obj):
        next = request.GET.get("next", None)
        self.clear_message(request)
        return redirect(next)

    def response_post_save_change(self, request, obj):
        next = request.GET.get("next", None)
        self.clear_message(request)
        return redirect(next)

    def demographics(self, obj=None):
        return mark_safe(f"{obj.get_gender_display()} {obj.age_in_years}yrs ")

    def clear_message(self, request):
        storage = messages.get_messages(request)
        for msg in storage:
            pass
        storage.used = True
