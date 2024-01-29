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
from ..constants import YES_TWO

from ..models import EnrollmentCRF


class EnrollmentCrfFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tb_treatment = self.cleaned_data.get("TB_treatment")
        self.tb_treatment_duration = self.cleaned_data.get("TB_treatment_duration")
        self.tb_treatment_regimen = self.cleaned_data.get("TB_treatment_regimen")
        self.tb_treatment_outcome = self.cleaned_data.get("TB_treatment_outcome")
        self.immuno_diseases = self.cleaned_data.get("immuno_diseases")
        self.immuno_diseases_specify = self.cleaned_data.get("immuno_diseases_specify")
        self.other_disease = self.cleaned_data.get("other_disease")
        self.other_disease_specify = self.cleaned_data.get("other_disease_specify")
        self.other_disease_specify_other = self.cleaned_data.get("other_disease_specify_other")
        self.resp_sample = self.cleaned_data.get("resp_sample")
        self.resp_sample_DST_date = self.cleaned_data.get("resp_sample_DST_date")
        self.resp_sample_type_DST = self.cleaned_data.get("resp_sample_type_DST")
        self.resp_sample_seq_date = self.cleaned_data.get("resp_sample_seq_date")
        self.resp_sample_type_seq = self.cleaned_data.get("resp_sample_type_seq")
        self.pleural_fluid = self.cleaned_data.get("pleural_fluid")
        self.pleural_fluid_date = self.cleaned_data.get("pleural_fluid_date")
        self.csf = self.cleaned_data.get("csf")
        self.csf_date = self.cleaned_data.get("csf_date")
        self.peritoneal_fluid = self.cleaned_data.get("peritoneal_fluid")
        self.peritoneal_fluid_date = self.cleaned_data.get("peritoneal_fluid_date")
        self.pericardial_fluid = self.cleaned_data.get("pericardial_fluid")
        self.pericardial_fluid_date = self.cleaned_data.get("pericardial_fluid_date")
        self.lymph_node_aspirate = self.cleaned_data.get("lymph_node_aspirate")
        self.lymph_node_aspirate_date = self.cleaned_data.get("lymph_node_aspirate_date")
        self.stool = self.cleaned_data.get("stool")
        self.stool_date = self.cleaned_data.get("stool_date")
        self.chest_xray = self.cleaned_data.get("chest_xray")
        self.chest_xray_date = self.cleaned_data.get("chest_xray_date")

    def clean(self):
        self.required_if(
            YES, field="TB_treatment", field_required="TB_treatment_duration"
        )
        self.required_if(
            YES, field="TB_treatment", field_required="TB_treatment_regimen"
        )
        self.required_if(
            YES, field="TB_treatment", field_required="TB_treatment_outcome"
        )
        self.required_if(
            YES, field="immuno_diseases", field_required="immuno_diseases_specify"
        )
        self.required_if(
            YES, field="other_disease", field_required="other_disease_specify"
        )
        self.required_if(
            OTHER, field="other_disease_specify", field_required="other_disease_specify_other"
        )
        self.not_required_if(NO, field="resp_sample",
                             field_not_required="resp_sample_DST_date")
        self.required_if(
            YES_TWO, field="resp_sample", field_required="resp_sample_seq_date"
        )
        self.required_if(
            YES_TWO, field="resp_sample", field_required="resp_sample_type_seq"
        )

        self.required_if(
            YES, field="other_disease", field_required="other_disease_specify"
        )
        # xxxxxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.required_if(
            YES, field="pleural_fluid", field_required="pleural_fluid_date"
        )
        self.required_if(
            YES, field="csf", field_required="csf_date"
        )
        self.required_if(
            YES, field="peritoneal_fluid", field_required="peritoneal_fluid_date"
        )
        self.required_if(
            YES, field="pericardial_fluid", field_required="pericardial_fluid_date"
        )
        self.required_if(
            YES, field="lymph_node_aspirate", field_required="lymph_node_aspirate_date"
        )
        self.required_if(
            YES, field="stool", field_required="stool_date"
        )
        self.required_if(
            YES, field="chest_xray", field_required="chest_xray_date"
        )


class EnrollmentCrfForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = EnrollmentCrfFormValidator

    class Meta:
        model = EnrollmentCRF
        fields = "__all__"
