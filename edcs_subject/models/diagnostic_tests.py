from django.db import models
from django.utils.safestring import mark_safe

from edcs_constants.choices import (
    YES_NO,
)

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import RESPIRATORY_YES, RESPIRATORY_REASONS, APPEARANCE, ACCESSION_STATUS, \
    AFB_TECHNIQUE, AFB_RESULTS, RIF_RESISTANCE, MTB, SPC_CT, NOT_REPEAT_REASONS, \
    DX_TEST_RESULTS
from ..model_mixins import CrfModelMixin


class DiagnosticTests(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )
    # ************************************ 1 *****************************
    sample_type_a = models.CharField(
        verbose_name="Sample type",
        max_length=85,
    )

    xpert_mtb_rif_a = models.CharField(
        verbose_name="Xpert MTB/RIF (Ultra)",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    truenat_mtb_plus_a = models.CharField(
        verbose_name="Truenat MTB Plus",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    culture_a = models.CharField(
        verbose_name="Culture MGIT/LJ",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    smear_microscopy_a = models.CharField(
        verbose_name="Smear microscopy	direct ZN/FM",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    mods_a = models.CharField(
        verbose_name="MODS",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    other_test_a = edcs_models.OtherCharField()

    other_test_result_a = models.CharField(
        verbose_name="Test result",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    # ************************************** 2 *************************************

    sample_type_b = models.CharField(
        verbose_name="Sample type",
        max_length=85,
    )

    xpert_mtb_rif_b = models.CharField(
        verbose_name="Xpert MTB/RIF (Ultra)",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    truenat_mtb_plus_b = models.CharField(
        verbose_name="Truenat MTB Plus",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    culture_b = models.CharField(
        verbose_name="Culture MGIT/LJ",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    smear_microscopy_b = models.CharField(
        verbose_name="Smear microscopy	direct ZN/FM",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    mods_b = models.CharField(
        verbose_name="MODS",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    other_test_b = edcs_models.OtherCharField()

    other_test_result_b = models.CharField(
        verbose_name="Test result",
        max_length=45,
        choices=DX_TEST_RESULTS,
    )

    remarks = models.TextField(
        verbose_name="Any remarks on any of the laboratory procedures above",
        blank=True,
        null=True,
    )

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Diagnostic Tests"
        verbose_name_plural = "Diagnostic Tests"
