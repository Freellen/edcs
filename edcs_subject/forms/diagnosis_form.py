from django import forms
from django.db.models import Q

from edcs_constants.constants import (
    NEVER,
    NOT_APPLICABLE,
    OTHER,
    YES,
    YES_CURRENT_CHEW,
    YES_CURRENT_SMOKER,
    YES_PAST_CHEW,
    YES_PAST_SMOKER, NO,
)
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator
from ..constants import YES_TWO, REFERRED_TREATMENT, NOT_STARTED

from ..models import DiagnosisCrf


class DiagnosisCrfFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tb_dx = self.cleaned_data.get("TB_dx")
        self.tb_dx_made = self.cleaned_data.get("TB_dx_made")
        self.tb_dx_made_other = self.cleaned_data.get("TB_dx_made_other")
        self.tb_dx_xpert_truenat_nga = self.cleaned_data.get("TB_dx_xpert_truenat_nga")
        self.tb_dx_xpert_truenat_nga_date = self.cleaned_data.get(
            "TB_dx_xpert_truenat_nga_date")
        self.tb_dx_other_tests = self.cleaned_data.get("TB_dx_other_tests")
        self.info_TB_dx_made = self.cleaned_data.get("info_TB_dx_made")
        self.info_TB_dx_made_other = self.cleaned_data.get("info_TB_dx_made_other")
        self.TB_treatment_start = self.cleaned_data.get("TB_treatment_start")
        self.TB_treatment_start_date = self.cleaned_data.get("TB_treatment_start_date")
        self.health_facility = self.cleaned_data.get("health_facility")
        self.reason_not_started = self.cleaned_data.get("reason_not_started")
        self.treatment_regimen = self.cleaned_data.get("treatment_regimen")
        self.treatment_regimen_other = self.cleaned_data.get("treatment_regimen_other")
        self.treatment_based_result = self.cleaned_data.get("treatment_based_result")
        self.treatment_based_result_other = self.cleaned_data.get("treatment_based_result_other")
        self.regimen_changed = self.cleaned_data.get("regimen_changed")
        self.regimen_changed_no = self.cleaned_data.get("regimen_changed_no")
        self.regimen_change1_date = self.cleaned_data.get("regimen_change1_date")
        self.regimen_change1 = self.cleaned_data.get("regimen_change1")
        self.regimen_change1_reasons = self.cleaned_data.get("regimen_change1_reasons")
        self.regimen_change2_date = self.cleaned_data.get("regimen_change2_date")
        self.regimen_change2 = self.cleaned_data.get("regimen_change2")
        self.regimen_change2_reasons = self.cleaned_data.get("regimen_change2_reasons")
        self.regimen_change3_date = self.cleaned_data.get("regimen_change3_date")
        self.regimen_change3 = self.cleaned_data.get("regimen_change3")
        self.regimen_change3_reasons = self.cleaned_data.get("regimen_change3_reasons")
        self.treatment_outcome = self.cleaned_data.get("treatment_outcome")
        self.other_dx = self.cleaned_data.get("other_dx")
        self.other_dx_pneumonia = self.cleaned_data.get("other_dx_pneumonia")
        self.other_dx_other = self.cleaned_data.get("other_dx_other")
        self.other_disease = self.cleaned_data.get("other_disease")

    def clean(self):
        self.required_if(
            YES, field="TB_dx", field_required="TB_dx_made"
        )
        self.required_if(
            OTHER, field="TB_dx_made", field_required="TB_dx_made_other"
        )
        self.required_if(
            YES, field="TB_dx", field_required="TB_dx_xpert_truenat_nga"
        )
        self.required_if(
            YES, field="TB_dx_xpert_truenat_nga", field_required="TB_dx_xpert_truenat_nga_date"
        )
        self.m2m_other_specify(
            OTHER, m2m_field="other_disease", field_other="info_TB_dx_made_other"
        )
        self.required_if(
            YES, field="TB_dx", field_required="TB_treatment_start"
        )
        self.not_required_if(YES, field="TB_treatment_start",
                             field_not_required="TB_treatment_start_date")
        self.required_if(
            REFERRED_TREATMENT, field="TB_treatment_start", field_required="health_facility"
        )
        self.required_if(
            NOT_STARTED, field="TB_treatment_start", field_required="reason_not_started"
        )

        self.required_if(
            YES, field="TB_treatment_start", field_required="treatment_regimen"
        )
        # xxxxxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.required_if(
            OTHER, field="treatment_regimen", field_required="treatment_regimen_other"
        )
        self.required_if(
            YES, field="TB_treatment_start", field_required="treatment_based_result"
        )
        self.required_if(
            OTHER, field="treatment_based_result", field_required="treatment_based_result_other"
        )
        self.required_if(
            YES, field="TB_treatment_start", field_required="regimen_changed"
        )
        self.required_if(
            YES, field="regimen_changed", field_required="regimen_changed_no"
        )
        self.required_if(
            YES, field="regimen_changed", field_required="regimen_change1_date"
        )
        self.required_if(
            YES, field="regimen_changed", field_required="regimen_change1"
        )
        self.required_if(
            YES, field="regimen_changed", field_required="regimen_change1_reasons"
        )
        self.required_if(
            YES, field="TB_dx", field_required="treatment_outcome"
        )
        self.m2m_other_specify(
            OTHER, m2m_field="other_dx", field_other="other_dx_other"
        )


class DiagnosisCrfForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DiagnosisCrfFormValidator

    class Meta:
        model = DiagnosisCrf
        fields = "__all__"
