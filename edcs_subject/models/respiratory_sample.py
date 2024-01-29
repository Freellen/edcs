from django.db import models
from django.utils.safestring import mark_safe

from edcs_constants.choices import (
    YES_NO,
)

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import RESPIRATORY_YES, RESPIRATORY_REASONS, APPEARANCE, ACCESSION_STATUS, \
    AFB_TECHNIQUE, AFB_RESULTS, RIF_RESISTANCE, MTB, SPC_CT, NOT_REPEAT_REASONS
from ..model_mixins import CrfModelMixin


class RespiratorySample(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    respiratory_sample = models.CharField(
        verbose_name="Is at least one respiratory sample available?",
        max_length=45,
        choices=YES_NO,
    )

    respiratory_sample_yes = models.CharField(
        verbose_name="If yes, How many?",
        max_length=45,
        choices=RESPIRATORY_YES,
    )

    respiratory_sample_no = models.CharField(
        verbose_name="If No, reason?",
        max_length=45,
        choices=RESPIRATORY_REASONS,
    )

    respiratory_sample_no_other = edcs_models.OtherCharField()

    respiratory_sample1_date = models.DateField(
        verbose_name=mark_safe("Date sample(1) collected"),
        null=True,
        blank=True,
    )

    respiratory_sample2_date = models.DateField(
        verbose_name=mark_safe("Date sample(2) collected"),
        null=True,
        blank=True,
    )

    respiratory_sample3_date = models.DateField(
        verbose_name=mark_safe("Date sample(3) collected"),
        null=True,
        blank=True,
    )

    sample_lab_receive_date = models.DateField(
        verbose_name=mark_safe("Date sample(s) received in the laboratory"),
        null=True,
        blank=True,
    )

    sputum_respiratory_sample = models.IntegerField(
        verbose_name="Sputum sample(s) received?",
        blank=True,
        null=True,
    )

    nga_respiratory_sample = models.IntegerField(
        verbose_name="NGA sample(s) received?",
        blank=True,
        null=True,
    )

    appearance = models.CharField(
        verbose_name="Appearance",
        max_length=45,
        null=True,
        blank=True,
        choices=APPEARANCE,
    )

    sample_volume = models.DecimalField(
        verbose_name="Approximate volume sample?",
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="in mL"
    )

    accession_status = models.CharField(
        verbose_name="Sample accession status?",
        max_length=45,
        choices=ACCESSION_STATUS,
    )

    afb_microscopy_date_a = models.DateField(
        verbose_name="AFB microscopy Date?",
        null=True,
        blank=True,
    )

    afb_technique_a = models.CharField(
        verbose_name=mark_safe("AFB technique?"),
        max_length=45,
        blank=True,
        null=True,
        choices=AFB_TECHNIQUE
    )

    afb_result_a = models.CharField(
        verbose_name="Results A?",
        max_length=80,
        null=True,
        blank=True,
        choices=AFB_RESULTS,
    )

    afb_microscopy_date_b = models.DateField(
        verbose_name="AFB microscopy Date?",
        null=True,
        blank=True,
    )

    afb_technique_b = models.CharField(
        verbose_name=mark_safe("AFB technique?"),
        max_length=45,
        blank=True,
        null=True,
        choices=AFB_TECHNIQUE
    )

    afb_result_b = models.CharField(
        verbose_name="Results B?",
        max_length=45,
        null=True,
        blank=True,
        choices=AFB_RESULTS,
    )

    xpert_mtb_date = models.DateField(
        verbose_name="Xpert MTB (Ultra) test result Date?",
        null=True,
        blank=True,
    )

    xpert_mtb = models.CharField(
        verbose_name="MTB",
        max_length=45,
        null=True,
        blank=True,
        choices=MTB,
    )

    mtb_error_code = models.CharField(
        verbose_name="MTB",
        max_length=125,
        null=True,
        blank=True,
        choices=MTB,
    )

    rif_resistance = models.CharField(
        verbose_name="RIF resistance",
        max_length=45,
        null=True,
        blank=True,
        choices=RIF_RESISTANCE,
    )

    spc_ct_available = models.CharField(
        verbose_name=mark_safe("Is Sample Processing Control (SPC) Cycle threshold (Ct) "
                               "value available"),
        max_length=80,
        choices=SPC_CT,
        blank=True,
        null=True,
    )

    spc_ct_value = models.CharField(
        verbose_name=mark_safe("Sample Processing Control (SPC) Cycle threshold (Ct) "
                               "value"),
        max_length=120,
        blank=True,
        null=True,
    )

    test_repeated = models.CharField(
        verbose_name="If no test result  was obtained, was the test repeated?",
        max_length=45,
        choices=YES_NO,
        blank=True,
        null=True,
    )

    test_repeated_date = models.DateField(
        verbose_name="Test repeated date?",
        blank=True,
        null=True,
    )

    test_not_repeated_reason = models.CharField(
        verbose_name="If No, specify reasons",
        max_length=45,
        choices=NOT_REPEAT_REASONS,
    )

    test_not_repeated_reason_other = edcs_models.OtherCharField()

# *****************************************

    repeat_xpert_mtb_date = models.DateField(
        verbose_name="Xpert MTB (Ultra) test result Date?",
        null=True,
        blank=True,
    )

    repeat_xpert_mtb = models.CharField(
        verbose_name="MTB",
        max_length=45,
        null=True,
        blank=True,
        choices=MTB,
    )

    repeat_mtb_error_code = models.CharField(
        verbose_name="MTB",
        max_length=125,
        null=True,
        blank=True,
        choices=MTB,
    )

    repeat_rif_resistance = models.CharField(
        verbose_name="RIF resistance",
        max_length=45,
        null=True,
        blank=True,
        choices=RIF_RESISTANCE,
    )

    repeat_spc_ct_available = models.CharField(
        verbose_name=mark_safe("SPC-Ct value available"),
        max_length=80,
        choices=SPC_CT,
        blank=True,
        null=True,
    )

    repeat_spc_ct_value = models.CharField(
        verbose_name=mark_safe("SPC-Ct value"),
        max_length=120,
        blank=True,
        null=True,
    )

    # ***********************************

    truenat_mtb_plus_date = models.DateField(
        verbose_name="Truenat MTB Plus/ Truenat MTB-RIF Dx test Date?",
        null=True,
        blank=True,
    )

    truenat_plus_mtb = models.CharField(
        verbose_name="MTB",
        max_length=45,
        null=True,
        blank=True,
        choices=MTB,
    )

    truenat_plus_error_code = models.CharField(
        verbose_name="MTB",
        max_length=125,
        null=True,
        blank=True,
        choices=MTB,
    )

    truenat_rif_resistance = models.CharField(
        verbose_name="RIF resistance",
        max_length=45,
        null=True,
        blank=True,
        choices=RIF_RESISTANCE,
    )

    truenat_spc_ct_available = models.CharField(
        verbose_name=mark_safe("Is Internal Positive Control (IPC) Cycle threshold (Ct) value available"),
        max_length=80,
        choices=SPC_CT,
        blank=True,
        null=True,
    )

    truenat_spc_ct_value = models.CharField(
        verbose_name=mark_safe("Internal Positive Control (IPC) Cycle threshold (Ct) value"),
        max_length=120,
        blank=True,
        null=True,
    )

    truenat_test_repeated = models.CharField(
        verbose_name="If no test result  was obtained, was the test repeated?",
        max_length=45,
        choices=YES_NO,
        blank=True,
        null=True,
    )

    truenat_test_repeated_date = models.DateField(
        verbose_name="Test repeated date?",
        blank=True,
        null=True,
    )

    truenat_test_not_repeated_reason = models.CharField(
        verbose_name="If No, specify reasons",
        max_length=45,
        choices=NOT_REPEAT_REASONS,
    )

    truenat_test_not_repeated_reason_other = edcs_models.OtherCharField()

    # *****************************************

    truenat_repeat_xpert_mtb_date = models.DateField(
        verbose_name="Xpert MTB (Ultra) test result Date?",
        null=True,
        blank=True,
    )

    truenat_repeat_xpert_mtb = models.CharField(
        verbose_name="MTB",
        max_length=45,
        null=True,
        blank=True,
        choices=MTB,
    )

    truenat_repeat_mtb_error_code = models.CharField(
        verbose_name="MTB",
        max_length=125,
        null=True,
        blank=True,
        choices=MTB,
    )

    truenat_repeat_rif_resistance = models.CharField(
        verbose_name="RIF resistance",
        max_length=45,
        null=True,
        blank=True,
        choices=RIF_RESISTANCE,
    )

    truenat_repeat_spc_ct_available = models.CharField(
        verbose_name=mark_safe("Is IPC-Ct value available"),
        max_length=80,
        choices=SPC_CT,
        blank=True,
        null=True,
    )

    truenat_repeat_spc_ct_value = models.CharField(
        verbose_name=mark_safe("IPC-Ct value"),
        max_length=120,
        blank=True,
        null=True,
    )

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Respiratory sample"
        verbose_name_plural = "Respiratory sample"
