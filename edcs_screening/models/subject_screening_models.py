from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.db import models
from django_crypto_fields.fields import EncryptedCharField

from edcs_constants.choices import COUNTRY, YES_NO
from edcs_model.models import BaseUuidModel, OtherCharField
from edcs_screening.model_mixins import ScreeningModelMixin
from edcs_screening.screening_identifier import ScreeningIdentifier

from ..choices import CLINIC, PATIENT_CATEGORY
from ..eligibility import check_eligible_final


class SubjectScreeningModelError(Exception):
    pass


class ScreeningIdentifier(ScreeningIdentifier):
    template = "S{random_string}"


class SubjectScreening(
    ScreeningModelMixin,
    BaseUuidModel,
):
    identifier_cls = ScreeningIdentifier

    patient_18yrs = models.CharField(
        verbose_name="Is the patient at least 18 years old?  ",
        max_length=15,
        choices=YES_NO,
    )

    symptoms_pulmonary = models.CharField(
        verbose_name="Does the patient present with signs and symptoms suggestive of "
                     "pulmonary TB or another pulmonary infection of bacterial, viral, or"
                     " fungal origin? ",
        max_length=15,
        choices=YES_NO
    )

    respiratory_sample = models.CharField(
        verbose_name=(
            "Is the patient capable of producing a respiratory sample? "
        ),
        max_length=15,
        choices=YES_NO,
    )
    consent = models.CharField(
        verbose_name="Has the patient provided written informed consent to participate? ",
        max_length=15,
        choices=YES_NO
    )
    patient_id = EncryptedCharField(
        verbose_name="Patients identification number:",
        max_length=50,
        blank=False,
        help_text="Country ID number,Driver license,Passport,Hospital number, etc."
    )

    patient_know_dob = models.CharField(
        verbose_name="Does the patient know his/her date of birth?",
        choices=YES_NO,
        max_length=50,
    )
    patient_dob = models.DateField(
        verbose_name="What is patient date of birth?",
        null=True,
        blank=True,
    )
    initials = EncryptedCharField(
        validators=[
            RegexValidator("[A-Z]{1,3}", "Invalid format"),
            MinLengthValidator(2),
            MaxLengthValidator(3),
        ],
        help_text="Use UPPERCASE letters only. May be 2 or 3 letters.",
        blank=False,
    )

    def save(self, *args, **kwargs):
        check_eligible_final(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Subject Screening"
        verbose_name_plural = "Subject Screening"
