from django import forms
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator
from ..constants import RESISTANT

from ..models import DrugSusceptibilityTests


class DrugSusceptibilityTestsFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phenotypic_rifampicin = self.cleaned_data.get("phenotypic_rifampicin")
        self.phenotypic_rifampicin_mic = self.cleaned_data.get("phenotypic_rifampicin_mic")

    def check(self, value1, value2):
        result = False
        if value1 or value2:
            result = True
        return result

    def clean(self):
        self.required_if(
            RESISTANT, field="phenotypic_rifampicin",
            field_required="phenotypic_rifampicin_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_isoniazid", field_required="phenotypic_isoniazid_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_levofloxacin", field_required="phenotypic_levofloxacin_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_moxifloxacin", field_required="phenotypic_moxifloxacin_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_bedaquiline", field_required="phenotypic_bedaquiline_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_linezolid", field_required="phenotypic_linezolid_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_clofazimine", field_required="phenotypic_clofazimine_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_cycloserine", field_required="phenotypic_cycloserine_mic"
        )

        self.required_if(
            RESISTANT, field="phenotypic_terizidone", field_required="phenotypic_terizidone_mic"
        )
        # xxxxxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.required_if(
            RESISTANT, field="phenotypic_ethambutol", field_required="phenotypic_ethambutol_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_delamanid", field_required="phenotypic_delamanid_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_pyrazinamide", field_required="phenotypic_pyrazinamide_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_imipenem_cilastatin", field_required="phenotypic_imipenem_cilastatin_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_meropenem", field_required="phenotypic_meropenem_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_amikacin", field_required="phenotypic_amikacin_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_streptomycin", field_required="phenotypic_streptomycin_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_ethionamide", field_required="phenotypic_ethionamide_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_prothionamide", field_required="phenotypic_prothionamide_mic"
        )
        self.required_if(
            RESISTANT, field="phenotypic_para_aminosalicylic", field_required="phenotypic_para_aminosalicylic_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_rifampicin", field_required="nanopore_rifampicin_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_isoniazid", field_required="nanopore_isoniazid_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_levofloxacin", field_required="nanopore_levofloxacin_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_moxifloxacin", field_required="nanopore_moxifloxacin_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_bedaquiline", field_required="nanopore_bedaquiline_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_linezolid", field_required="nanopore_linezolid_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_clofazimine", field_required="nanopore_clofazimine_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_cycloserine", field_required="nanopore_cycloserine_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_terizidone", field_required="nanopore_terizidone_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_ethambutol", field_required="nanopore_ethambutol_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_delamanid", field_required="nanopore_delamanid_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_pyrazinamide", field_required="nanopore_pyrazinamide_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_imipenem_cilastatin", field_required="nanopore_imipenem_cilastatin_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_meropenem", field_required="nanopore_meropenem_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_amikacin", field_required="nanopore_amikacin_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_streptomycin", field_required="nanopore_streptomycin_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_ethionamide", field_required="nanopore_ethionamide_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_prothionamide", field_required="nanopore_prothionamide_mic"
        )
        self.required_if(
            RESISTANT, field="nanopore_para_aminosalicylic", field_required="nanopore_para_aminosalicylic_mic"
        )


class DrugSusceptibilityTestsForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DrugSusceptibilityTestsFormValidator

    class Meta:
        model = DrugSusceptibilityTests
        fields = "__all__"
