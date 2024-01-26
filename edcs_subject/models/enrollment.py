from django.db import models
from django.utils.safestring import mark_safe

from edcs_constants.choices import (
    HIV_RESULT_DWTA_DONT_KNOW,
    YES_NO,
    YES_NO_DWTA_DONT_KNOW, YES_NO_NA, YES_NO_DECLINED_TO_ANSWER_NA,
)
from edcs_constants.constants import NOT_APPLICABLE
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import LUNG_DISEASE, MISS_ARV
from ..model_mixins import CrfModelMixin


class EnrollmentCRF(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    hiv_test = models.CharField(
        verbose_name="Cough of >2 weeks?",
        max_length=45,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    hiv_test_date = models.DateField(
        verbose_name="Poor weight gain or loss of weight?",
        null=True,
        blank=True,
    )

    hiv_dx = models.CharField(
        verbose_name=mark_safe("What was the result of your most recent HIV test?"),
        max_length=45,
        choices=HIV_RESULT_DWTA_DONT_KNOW,
        default=NOT_APPLICABLE,
    )
    arv = models.CharField(
        verbose_name=mark_safe("Coughing up blood "),
        max_length=45,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    arv_start_date = models.DateField(
        verbose_name="Unexplained fever",
        null=True,
        blank=True,
    )

    arv_regularly = models.CharField(
        verbose_name=mark_safe("Drenching night sweats"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    miss_taking_arv = models.CharField(
        verbose_name=mark_safe("Lymph nodes in neck enlarged"),
        max_length=45,
        choices=MISS_ARV,
        default=NOT_APPLICABLE,
    )

    miss_taking_arv_other = edcs_models.OtherCharField()

    lung_diseases_dx = models.CharField(
        verbose_name="Contact history with infectious TB patient",
        max_length=45,
        choices=LUNG_DISEASE,
    )

    copd_dx_date = models.DateField(
        verbose_name="Was the participant treated for TB before?",
        null=True,
        blank=True,
    )

    asthma_dx_date = models.DateField(
        verbose_name="How long ago was the participant treated for TB?",
        null=True,
        blank=True,
    )
    interstitial_lung_disease_dx_date = models.DateField(
        verbose_name="Which treatment regimen and duration was used?",
        null=True,
        blank=True,
    )

    use_lung_diseases_medication = models.CharField(
        verbose_name="What was the treatment outcome?",
        choices=YES_NO_DECLINED_TO_ANSWER_NA,
        max_length=80,
        default=NOT_APPLICABLE,
    )

    lung_diseases_medication = models.TextField(
        verbose_name="If is yes, what medications are you using?",
        null=True,
        blank=True,
    )

    htn_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with Hypertension?",
        max_length=45,
        choices=YES_NO,
    )

    htn_dx_date = models.DateField(
        verbose_name="If yes, when were you diagnosed?",
        null=True,
        blank=True,
    )

    use_htn_medication = models.CharField(
        verbose_name="Are you using any medications?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER_NA,
        default=NOT_APPLICABLE
    )

    htn_medication = models.TextField(
        verbose_name="If yes, what are you using currently?",
        null=True,
        blank=True,
    )

    dm_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with have Diabetes Mellitus? ",
        max_length=15,
        choices=YES_NO,
    )

    dm_dx_date = models.DateField(
        verbose_name="If yes, when were you diagnosed?",
        null=True,
        blank=True,
    )

    use_dm_medication = models.CharField(
        verbose_name="Are you using any medications?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER_NA,
        default=NOT_APPLICABLE
    )

    dm_medication = models.TextField(
        verbose_name="If is yes, what medications are you using currently?",
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Enrollment CRF"
        verbose_name_plural = "Enrollment CRF"
