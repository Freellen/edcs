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

from ..models import DiagnosticTests


class DiagnosticTestsFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sample_type_a = self.cleaned_data.get("sample_type_a")
        self.xpert_mtb_rif_a = self.cleaned_data.get("xpert_mtb_rif_a")
        self.truenat_mtb_plus_a = self.cleaned_data.get("truenat_mtb_plus_a")
        self.culture_a = self.cleaned_data.get("culture_a")
        self.smear_microscopy_a = self.cleaned_data.get("smear_microscopy_a")
        self.mods_a = self.cleaned_data.get("mods_a")
        self.other_test_a = self.cleaned_data.get("other_test_a")
        self.other_test_result_a = self.cleaned_data.get("other_test_result_a")
        self.sample_type_b = self.cleaned_data.get("sample_type_b")
        self.xpert_mtb_rif_b = self.cleaned_data.get("xpert_mtb_rif_b")
        self.truenat_mtb_plus_b = self.cleaned_data.get("truenat_mtb_plus_b")
        self.culture_b = self.cleaned_data.get("culture_b")
        self.smear_microscopy_b = self.cleaned_data.get("smear_microscopy_b")
        self.mods_b = self.cleaned_data.get("mods_b")
        self.other_test_b = self.cleaned_data.get("other_test_b")
        self.other_test_result_b = self.cleaned_data.get("other_test_result_b")

    def clean(self):
        self.required_if(
            OTHER, field="mods_a", field_required="other_test_a"
        )
        self.required_if(
            OTHER, field="mods_b", field_required="other_test_b"
        )


class DiagnosticTestsForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DiagnosticTestsFormValidator

    class Meta:
        model = DiagnosticTests
        fields = "__all__"
