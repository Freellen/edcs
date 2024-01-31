from django import forms
from django.db.models import Q

from edcs_constants.constants import (
    OTHER,
    YES, NO, ERROR,
)
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator
from ..constants import YES_TWO, TWO, THREE, NO_SPC

from ..models import RespiratorySample


class RespiratorySampleFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.respiratory_sample = self.cleaned_data.get("respiratory_sample")
        self.respiratory_sample_yes = self.cleaned_data.get("respiratory_sample_yes")
        self.respiratory_sample_no = self.cleaned_data.get("respiratory_sample_no")
        self.respiratory_sample_no_other = self.cleaned_data.get("respiratory_sample_no_other")
        self.respiratory_sample1_date = self.cleaned_data.get("respiratory_sample1_date")
        self.respiratory_sample2_date = self.cleaned_data.get("respiratory_sample2_date")
        self.respiratory_sample3_date = self.cleaned_data.get("respiratory_sample3_date")
        self.sample_lab_receive_date = self.cleaned_data.get("sample_lab_receive_date")
        self.sputum_respiratory_sample = self.cleaned_data.get("sputum_respiratory_sample")
        self.nga_respiratory_sample = self.cleaned_data.get("nga_respiratory_sample")
        self.appearance = self.cleaned_data.get("appearance")
        self.sample_volume = self.cleaned_data.get("sample_volume")
        self.accession_status = self.cleaned_data.get("accession_status")
        self.afb_microscopy_date_a = self.cleaned_data.get("afb_microscopy_date_a")
        self.afb_technique_a = self.cleaned_data.get("afb_technique_a")
        self.afb_result_a = self.cleaned_data.get("afb_result_a")
        self.afb_microscopy_date_b = self.cleaned_data.get("afb_microscopy_date_b")
        self.afb_technique_b = self.cleaned_data.get("afb_technique_b")
        self.afb_result_b = self.cleaned_data.get("afb_result_b")

    def clean(self):
        self.applicable_if(
            YES, field="respiratory_sample", field_applicable="respiratory_sample_yes"
        )
        self.applicable_if(
            NO, field="respiratory_sample", field_applicable="respiratory_sample_no"
        )
        self.required_if(
            OTHER, field="respiratory_sample_no", field_required="respiratory_sample_no_other"
        )
        self.applicable_if(
            YES, field="respiratory_sample", field_applicable="respiratory_sample1_date"
        )
        # self.required_if(
        #     TWO, field="respiratory_sample_yes", field_required="respiratory_sample2_date"
        # )
        if self.respiratory_sample_yes == TWO:
            self.required_if(
                TWO, field="respiratory_sample_yes", field_required="respiratory_sample2_date"
            )
        if self.respiratory_sample_yes == THREE:
            self.required_if(
                THREE, field="respiratory_sample_yes",
                field_required="respiratory_sample3_date"
            )
            self.respiratory_sample_yes = TWO
            self.required_if(
                TWO, field="respiratory_sample_yes", field_required="respiratory_sample2_date"
            )

        self.required_if(
            YES, field="respiratory_sample", field_required="sample_lab_receive_date"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="sputum_respiratory_sample"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="nga_respiratory_sample"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="appearance"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="sample_volume"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="accession_status"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="afb_microscopy_date_a"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="afb_technique_a"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="afb_result_a"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="afb_microscopy_date_b"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="afb_technique_b"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="afb_result_b"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="xpert_mtb_date"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="xpert_mtb"
        )
        self.required_if(
            ERROR, field="xpert_mtb", field_required="mtb_error_code"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="rif_resistance"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="spc_ct_available"
        )
        self.required_if(
            YES, field="spc_ct_available", field_required="spc_ct_value"
        )
        self.required_if(
            YES, field="spc_ct_available", field_required="spc_ct_value"
        )
        self.required_if(
            NO_SPC, field="spc_ct_available", field_required="test_repeated"
        )
        self.required_if(
            YES, field="test_repeated", field_required="test_repeated_date"
        )
        self.applicable_if(
            NO, field="test_repeated", field_applicable="test_not_repeated_reason"
        )
        self.required_if(
            OTHER, field="test_not_repeated_reason",
            field_required="test_not_repeated_reason_other"
        )
        self.required_if(
            YES, field="test_repeated", field_required="repeat_xpert_mtb_date"
        )
        self.required_if(
            YES, field="test_repeated", field_required="repeat_xpert_mtb"
        )
        self.required_if(
            OTHER, field="repeat_xpert_mtb", field_required="repeat_mtb_error_code"
        )
        self.required_if(
            YES, field="test_repeated", field_required="repeat_rif_resistance"
        )
        self.required_if(
            YES, field="test_repeated", field_required="repeat_spc_ct_available"
        )
        self.required_if(
            YES, field="test_repeated", field_required="repeat_spc_ct_value"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="truenat_mtb_plus_date"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="truenat_plus_mtb"
        )
        self.required_if(
            ERROR, field="truenat_plus_mtb", field_required="truenat_plus_error_code"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="truenat_rif_resistance"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="truenat_spc_ct_available"
        )
        self.required_if(
            YES, field="truenat_spc_ct_available", field_required="truenat_spc_ct_value"
        )
        self.required_if(
            YES, field="respiratory_sample", field_required="truenat_test_repeated"
        )
        self.required_if(
            YES, field="truenat_test_repeated", field_required="truenat_test_repeated_date"
        )
        self.applicable_if(
            NO, field="truenat_test_repeated",
            field_applicable="truenat_test_not_repeated_reason"
        )
        self.required_if(
            OTHER, field="truenat_test_not_repeated_reason",
            field_required="truenat_test_not_repeated_reason_other"
        )
        self.required_if(
            YES, field="truenat_test_repeated", field_required="truenat_repeat_xpert_mtb_date"
        )
        self.required_if(
            YES, field="truenat_test_repeated", field_required="truenat_repeat_xpert_mtb"
        )
        self.required_if(
            YES, field="truenat_repeat_xpert_mtb",
            field_required="truenat_repeat_mtb_error_code"
        )
        self.required_if(
            YES, field="truenat_test_repeated", field_required="truenat_repeat_rif_resistance"
        )
        self.required_if(
            YES, field="truenat_test_repeated",
            field_required="truenat_repeat_spc_ct_available"
        )
        self.required_if(
            YES, field="truenat_repeat_spc_ct_available",
            field_required="truenat_repeat_spc_ct_value"
        )


class RespiratorySampleForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = RespiratorySampleFormValidator

    class Meta:
        model = RespiratorySample
        fields = "__all__"
