from django.db import models

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import  MIC, XPERT_MTB_RIF, XPERT_XDR_INH, XPERT_XDR_FLQ, XPERT_XDR_AMK, \
    XPERT_XDR_KAN, XPERT_XDR_CAP, XPERT_XDR_ETH, MTBDR_PLUS, MTBDRSI
from ..model_mixins import CrfModelMixin


class DrugSusceptibilityTests(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    phenotypic_rifampicin = models.CharField(
        verbose_name="Rifampicin",
        max_length=45,
        choices=MIC,
    )

    phenotypic_rifampicin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_isoniazid = models.CharField(
        verbose_name="Isoniazid",
        max_length=45,
        choices=MIC,
    )

    phenotypic_isoniazid_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_levofloxacin = models.CharField(
        verbose_name="Levofloxacin",
        max_length=45,
        choices=MIC,
    )

    phenotypic_levofloxacin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_moxifloxacin = models.CharField(
        verbose_name="Moxifloxacin",
        max_length=45,
        choices=MIC,
    )

    phenotypic_moxifloxacin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_bedaquiline = models.CharField(
        verbose_name="Bedaquiline",
        max_length=45,
        choices=MIC,
    )

    phenotypic_bedaquiline_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_linezolid = models.CharField(
        verbose_name="Linezolid",
        max_length=45,
        choices=MIC,
    )

    phenotypic_linezolid_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_clofazimine = models.CharField(
        verbose_name="Clofazimine",
        max_length=45,
        choices=MIC,
    )

    phenotypic_clofazimine_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_cycloserine = models.CharField(
        verbose_name="Cycloserine",
        max_length=45,
        choices=MIC,
    )

    phenotypic_cycloserine_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_terizidone = models.CharField(
        verbose_name="Terizidone",
        max_length=45,
        choices=MIC,
    )

    phenotypic_terizidone_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_ethambutol = models.CharField(
        verbose_name="Ethambutol",
        max_length=45,
        choices=MIC,
    )

    phenotypic_ethambutol_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_delamanid = models.CharField(
        verbose_name="Delamanid",
        max_length=45,
        choices=MIC,
    )

    phenotypic_delamanid_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_pyrazinamide = models.CharField(
        verbose_name="Pyrazinamide",
        max_length=45,
        choices=MIC,
    )

    phenotypic_pyrazinamide_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_imipenem_cilastatin = models.CharField(
        verbose_name="Imipenem-cilastatin",
        max_length=45,
        choices=MIC,
    )

    phenotypic_imipenem_cilastatin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_meropenem = models.CharField(
        verbose_name="Meropenem",
        max_length=45,
        choices=MIC,
    )

    phenotypic_meropenem_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_amikacin = models.CharField(
        verbose_name="Amikacin",
        max_length=45,
        choices=MIC,
    )

    phenotypic_amikacin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_streptomycin = models.CharField(
        verbose_name="Streptomycin",
        max_length=45,
        choices=MIC,
    )

    phenotypic_streptomycin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_ethionamide = models.CharField(
        verbose_name="Ethionamide",
        max_length=45,
        choices=MIC,
    )

    phenotypic_ethionamide_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_prothionamide = models.CharField(
        verbose_name="Prothionamide",
        max_length=45,
        choices=MIC,
    )

    phenotypic_prothionamide_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    phenotypic_para_aminosalicylic = models.CharField(
        verbose_name="Para-aminosalicylic acid",
        max_length=45,
        choices=MIC,
    )

    phenotypic_para_aminosalicylic_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    xpert_mtb_refampicin = models.CharField(
        verbose_name="Refampicin",
        max_length=45,
        choices=XPERT_MTB_RIF,
    )

    xpert_xdr_isoniazid = models.CharField(
        verbose_name="Isoniazid",
        max_length=45,
        choices=XPERT_XDR_INH,
    )

    xpert_xdr_fluoroquinolones = models.CharField(
        verbose_name="Fluoroquinolones",
        max_length=45,
        choices=XPERT_XDR_FLQ,
    )

    xpert_xdr_amikacin = models.CharField(
        verbose_name="Amikacin",
        max_length=45,
        choices=XPERT_XDR_AMK,
    )

    xpert_xdr_kanamycin = models.CharField(
        verbose_name="Kanamycin",
        max_length=45,
        choices=XPERT_XDR_KAN,
    )

    xpert_xdr_capreomycin = models.CharField(
        verbose_name="Capreomycin",
        max_length=45,
        choices=XPERT_XDR_CAP,
    )

    xpert_xdr_ethionamide = models.CharField(
        verbose_name="Ethionamide",
        max_length=45,
        choices=XPERT_XDR_ETH,
    )

    nanopore_rifampicin = models.CharField(
        verbose_name="Rifampicin",
        max_length=45,
        choices=MIC,
    )

    nanopore_rifampicin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_isoniazid = models.CharField(
        verbose_name="Isoniazid",
        max_length=45,
        choices=MIC,
    )

    nanopore_isoniazid_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_levofloxacin = models.CharField(
        verbose_name="Levofloxacin",
        max_length=45,
        choices=MIC,
    )

    nanopore_levofloxacin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_moxifloxacin = models.CharField(
        verbose_name="Moxifloxacin",
        max_length=45,
        choices=MIC,
    )

    nanopore_moxifloxacin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_bedaquiline = models.CharField(
        verbose_name="Bedaquiline",
        max_length=45,
        choices=MIC,
    )

    nanopore_bedaquiline_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_linezolid = models.CharField(
        verbose_name="Linezolid",
        max_length=45,
        choices=MIC,
    )

    nanopore_linezolid_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_clofazimine = models.CharField(
        verbose_name="Clofazimine",
        max_length=45,
        choices=MIC,
    )

    nanopore_clofazimine_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_cycloserine = models.CharField(
        verbose_name="Cycloserine",
        max_length=45,
        choices=MIC,
    )

    nanopore_cycloserine_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_terizidone = models.CharField(
        verbose_name="Terizidone",
        max_length=45,
        choices=MIC,
    )

    nanopore_terizidone_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_ethambutol = models.CharField(
        verbose_name="Ethambutol",
        max_length=45,
        choices=MIC,
    )

    nanopore_ethambutol_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_delamanid = models.CharField(
        verbose_name="Delamanid",
        max_length=45,
        choices=MIC,
    )

    nanopore_delamanid_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_pyrazinamide = models.CharField(
        verbose_name="Pyrazinamide",
        max_length=45,
        choices=MIC,
    )

    nanopore_pyrazinamide_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_imipenem_cilastatin = models.CharField(
        verbose_name="Imipenem-cilastatin",
        max_length=45,
        choices=MIC,
    )

    nanopore_imipenem_cilastatin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_meropenem = models.CharField(
        verbose_name="Meropenem",
        max_length=45,
        choices=MIC,
    )

    nanopore_meropenem_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_amikacin = models.CharField(
        verbose_name="Amikacin",
        max_length=45,
        choices=MIC,
    )

    nanopore_amikacin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_streptomycin = models.CharField(
        verbose_name="Streptomycin",
        max_length=45,
        choices=MIC,
    )

    nanopore_streptomycin_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_ethionamide = models.CharField(
        verbose_name="Ethionamide",
        max_length=45,
        choices=MIC,
    )

    nanopore_ethionamide_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_prothionamide = models.CharField(
        verbose_name="Prothionamide",
        max_length=45,
        choices=MIC,
    )

    nanopore_prothionamide_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    nanopore_para_aminosalicylic = models.CharField(
        verbose_name="Para-aminosalicylic acid",
        max_length=45,
        choices=MIC,
    )

    nanopore_para_aminosalicylic_mic = models.CharField(
        verbose_name="MIC",
        max_length=125,
    )

    genotype_mtbdrplus = models.CharField(
        verbose_name="Line probe assay (1st line drugs). (GenoType MTBDRplus V2). "
                     "Indicate bands visible on the strip",
        max_length=125,
        choices=MTBDR_PLUS,
    )

    genotype_mtbdrsi = models.CharField(
        verbose_name="Line probe assay (2nd line drugs).(GenoType MTBDRsl V2). "
                     "Indicate bands visible on the strip",
        max_length=125,
        choices=MTBDRSI,
    )

    nanopore_version_number = models.CharField(
        verbose_name="Version number",
        max_length=45,
    )

    nanopore_lot_number = models.CharField(
        verbose_name="Lot number",
        max_length=45,
    )

    nanopore_resistance_detected = models.TextField(
        verbose_name="Specify drug resistance mutations detected",
    )

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Drug susceptibility Test"
        verbose_name_plural = "Drug susceptibility Test"
