from django.db import models
from django.utils.safestring import mark_safe

from edcs_constants.choices import (
    YES_NO,
)
from edcs_lists.models import InfoTbDxMade, OtherDxMade
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import TB_DIAGNOSIS_MADE, \
    TB_TREATMENT_START, TREATMENT_REGIMEN, TREATMENT_REGIMEN_BASED, TREATMENT_OUTCOME
from ..model_mixins import CrfModelMixin


class DiagnosisCrf(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    TB_dx = models.CharField(
        verbose_name="Was a TB diagnosis made?",
        max_length=45,
        choices=YES_NO,
    )

    TB_dx_made = models.CharField(
        verbose_name="How was the TB diagnosis made?",
        max_length=45,
        choices=TB_DIAGNOSIS_MADE,
    )

    TB_dx_made_other = edcs_models.OtherCharField()

    TB_dx_xpert_truenat_nga = models.CharField(
        verbose_name=mark_safe("On what test result(s) was the bacteriological diagnosis "
                               "based on Xpert/Truenat on sputum/NGA?"),
        max_length=45,
        choices=YES_NO,
    )

    TB_dx_xpert_truenat_nga_date = models.DateField(
        verbose_name="Date (Xpert/Truenat on sputum/NGA) result received by clinician",
        null=True,
        blank=True,
    )

    TB_dx_other_tests = models.TextField(
        verbose_name="Other test(s) with respective dates?",
        null=True,
        blank=True,
    )

    info_TB_dx_made = models.ManyToManyField(
        InfoTbDxMade,
        verbose_name="In case TB was diagnosed clinically, based on what information was the diagnosis made?",
    )

    info_TB_dx_made_other = edcs_models.OtherCharField()

    TB_treatment_start = models.CharField(
        verbose_name="Was TB treatment started?",
        max_length=45,
        choices=TB_TREATMENT_START,
    )

    TB_treatment_start_date = models.DateField(
        verbose_name="If yes, treatment start date?",
        null=True,
        blank=True,
    )

    health_facility = models.CharField(
        verbose_name=mark_safe("If referred  for treatment, name of the health facility?"),
        max_length=45,
        blank=True,
        null=True
    )

    reason_not_started = models.TextField(
        verbose_name="If Not started, specify reasons?",
        null=True,
        blank=True,
    )

    treatment_regimen = models.CharField(
        verbose_name=mark_safe("What treatment regimen was prescribed?"),
        max_length=45,
        choices=TREATMENT_REGIMEN,
    )

    treatment_regimen_other = edcs_models.OtherCharField()

    treatment_based_result = models.CharField(
        verbose_name="On what test result was the treatment regimen based and when did this test result become available to you? ",
        max_length=45,
        choices=TREATMENT_REGIMEN_BASED,
    )

    treatment_based_result_other = edcs_models.OtherCharField()

    regimen_changed = models.CharField(
        verbose_name="Was the regimen changed during the treatment?",
        max_length=45,
        choices=YES_NO,
    )

    regimen_changed_no = models.IntegerField(
        verbose_name="If yes, How many times regimen changed during the treatment?",
        null=True,
        blank=True,
    )

    regimen_change1_date = models.DateField(
        verbose_name="Date",
        null=True,
        blank=True,
    )

    regimen_change1 = models.CharField(
        verbose_name="Change introduced to the regimen",
        max_length=80,
        null=True,
        blank=True,
    )

    regimen_change1_reasons = models.TextField(
        verbose_name="Reason for change?",
        null=True,
        blank=True,
    )

    regimen_change2_date = models.DateField(
        verbose_name="Date",
        null=True,
        blank=True,
    )

    regimen_change2 = models.CharField(
        verbose_name="Change introduced to the regimen",
        max_length=80,
        null=True,
        blank=True,
    )

    regimen_change2_reasons = models.TextField(
        verbose_name="Reason for change?",
        null=True,
        blank=True,
    )

    regimen_change3_date = models.DateField(
        verbose_name="Date",
        null=True,
        blank=True,
    )

    regimen_change3 = models.CharField(
        verbose_name="Change introduced to the regimen",
        max_length=80,
        null=True,
        blank=True,
    )

    regimen_change3_reasons = models.TextField(
        verbose_name="Reason for change?",
        null=True,
        blank=True,
    )

    treatment_outcome = models.CharField(
        verbose_name="Treatment outcome at the end of treatment?",
        max_length=15,
        choices=TREATMENT_OUTCOME,
    )

    other_dx = models.ManyToManyField(
        OtherDxMade,
        verbose_name="What diagnosis other than TB was made?",
    )

    other_dx_pneumonia = models.DateField(
        verbose_name="If Bacterial pneumonia, please specify causative species if known?",
        null=True,
        blank=True,
    )

    other_dx_other = edcs_models.OtherCharField()

    other_disease = models.CharField(
        verbose_name="How was this diagnosis made?",
        max_length=115,
    )

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Diagnosis CRF"
        verbose_name_plural = "Diagnosis CRF"
