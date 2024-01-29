from django.db import models
from django.utils.safestring import mark_safe

from edcs_constants.choices import (
    YES_NO, POS_NEG_ONLY, YES_NO_UNKNOWN,
)
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import MEDICAL_CONDITIONS, RESPIRATORY_SAMPLES
from ..model_mixins import CrfModelMixin


class EnrollmentCRF(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    cough = models.CharField(
        verbose_name="Cough of >2 weeks?",
        max_length=45,
        choices=YES_NO,
    )

    weight_gain_loss = models.CharField(
        verbose_name="Poor weight gain or loss of weight?",
        max_length=45,
        choices=YES_NO,
    )

    cough_blood = models.CharField(
        verbose_name=mark_safe("Coughing up blood?"),
        max_length=45,
        choices=YES_NO,
    )

    fever = models.CharField(
        verbose_name="Unexplained fever?",
        max_length=45,
        choices=YES_NO,
    )

    night_sweat = models.CharField(
        verbose_name=mark_safe("Drenching night sweats?"),
        max_length=15,
        choices=YES_NO,
    )

    neck_enlarged = models.CharField(
        verbose_name=mark_safe("Lymph nodes in neck enlarged?"),
        max_length=45,
        choices=YES_NO,
    )

    contact_TB_patient = models.CharField(
        verbose_name="Contact history with infectious TB patient",
        max_length=45,
        choices=YES_NO,
    )

    TB_treatment = models.CharField(
        verbose_name="Was the participant treated for TB before?",
        max_length=45,
        choices=YES_NO,
    )

    TB_treatment_duration = models.CharField(
        verbose_name="How long ago was the participant treated for TB?",
        max_length=200,
        null=True,
        blank=True,
    )

    TB_treatment_regimen = models.TextField(
        verbose_name="Which treatment regimen and duration was used?",
        null=True,
        blank=True,
    )

    TB_treatment_outcome = models.CharField(
        verbose_name="What was the treatment outcome?",
        max_length=80,
        null=True,
        blank=True,
    )

    hiv_status = models.CharField(
        verbose_name="HIV status?",
        max_length=15,
        choices=POS_NEG_ONLY,
    )

    immuno_diseases = models.CharField(
        verbose_name="Other immunosuppressing diseases?",
        max_length=45,
        choices=YES_NO_UNKNOWN,
    )

    immuno_diseases_specify = models.TextField(
        verbose_name="If yes, to immunosuppressing diseases, please specify?",
        null=True,
        blank=True,
    )

    other_disease = models.CharField(
        verbose_name="Other relevant disease/medical condition?",
        max_length=45,
        choices=YES_NO_UNKNOWN,
    )

    other_disease_specify = models.CharField(
        verbose_name="If yes, to other relevant disease/medical condition?",
        max_length=45,
        null=True,
        blank=True,
        choices=MEDICAL_CONDITIONS,
    )

    other_disease_specify_other = edcs_models.OtherCharField()

    resp_sample = models.CharField(
        verbose_name="After TB was confirmed by a rapid molecular test, were two additional respiratory samples collected?",
        max_length=45,
        choices=RESPIRATORY_SAMPLES,
    )

    resp_sample_DST_date = models.DateField(
        verbose_name="Date of Sample for standard DST sample collection",
        null=True,
        blank=True,
    )

    resp_sample_type_DST = models.CharField(
        verbose_name="Sample type",
        max_length=200,
        null=True,
        blank=True,
    )

    resp_sample_seq_date = models.DateField(
        verbose_name="Date of Sample for sequencing collection",
        null=True,
        blank=True,
        help_text="only if two samples were collected"
    )

    resp_sample_type_seq = models.CharField(
        verbose_name="Sample type",
        max_length=200,
        null=True,
        blank=True,
        help_text="only if two samples were collected"
    )

    pleural_fluid = models.CharField(
        verbose_name="Was pleural fluid sample requested?",
        max_length=45,
        choices=YES_NO,
    )

    pleural_fluid_date = models.DateField(
        verbose_name="Date were pleural fluid sample requested",
        null=True,
        blank=True,
    )

    csf = models.CharField(
        verbose_name="Was Cerebral spinal fluid (CSF) sample requested?",
        max_length=45,
        choices=YES_NO,
    )

    csf_date = models.DateField(
        verbose_name="Date were Cerebral spinal fluid (CSF) sample requested",
        null=True,
        blank=True,
    )

    peritoneal_fluid = models.CharField(
        verbose_name="Was Cerebral Peritoneal fluid sample requested?",
        max_length=45,
        choices=YES_NO,
    )

    peritoneal_fluid_date = models.DateField(
        verbose_name="Date were Peritoneal fluid sample requested",
        null=True,
        blank=True,
    )

    pericardial_fluid = models.CharField(
        verbose_name="Was Pericardial fluid sample requested?",
        max_length=45,
        choices=YES_NO,
    )

    pericardial_fluid_date = models.DateField(
        verbose_name="Date were Pericardial fluid sample requested",
        null=True,
        blank=True,
    )

    lymph_node_aspirate = models.CharField(
        verbose_name="Was Lymph node aspirate sample requested?",
        max_length=45,
        choices=YES_NO,
    )

    lymph_node_aspirate_date = models.DateField(
        verbose_name="Date were Lymph node aspirate sample requested",
        null=True,
        blank=True,
    )

    stool = models.CharField(
        verbose_name="Was Stool sample requested?",
        max_length=45,
        choices=YES_NO,
    )

    stool_date = models.DateField(
        verbose_name="Date were Stool sample requested",
        null=True,
        blank=True,
    )

    other_requested_sample = models.TextField(
        verbose_name="Any other diagnostic samples requested?",
        null=True,
        blank=True,
    )

    chest_xray = models.CharField(
        verbose_name="Was chest X-ray requested?",
        max_length=45,
        choices=YES_NO,
    )

    chest_xray_date = models.DateField(
        verbose_name="If yes to chest x-ray, please specify date",
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Enrollment CRF"
        verbose_name_plural = "Enrollment CRF"
