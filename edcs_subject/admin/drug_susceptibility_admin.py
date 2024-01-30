from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import DrugSusceptibilityTestsForm
from ..models import DrugSusceptibilityTests
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DrugSusceptibilityTests, site=edcs_subject_admin)
class SubjectDrugSusceptibilityAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = DrugSusceptibilityTestsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Reason(s) for being regarded a presumptive TB patient at initial assessment",
            {
                "fields": (
                    "phenotypic_rifampicin",
                    "phenotypic_rifampicin_mic",
                    "phenotypic_isoniazid",
                    "phenotypic_isoniazid_mic",
                    "phenotypic_levofloxacin",
                    "phenotypic_levofloxacin_mic",
                    "phenotypic_moxifloxacin",
                    "phenotypic_moxifloxacin_mic",
                    "phenotypic_bedaquiline",
                    "phenotypic_bedaquiline_mic",
                    "phenotypic_linezolid",
                    "phenotypic_linezolid_mic",
                    "phenotypic_clofazimine",
                    "phenotypic_clofazimine_mic",
                    "phenotypic_cycloserine",
                    "phenotypic_cycloserine_mic",
                    "phenotypic_terizidone",
                    "phenotypic_terizidone_mic",
                    "phenotypic_ethambutol",
                    "phenotypic_ethambutol_mic",
                    "phenotypic_delamanid",
                    "phenotypic_delamanid_mic",
                    "phenotypic_pyrazinamide",
                    "phenotypic_pyrazinamide_mic",
                    "phenotypic_imipenem_cilastatin",
                    "phenotypic_imipenem_cilastatin_mic",
                    "phenotypic_meropenem",
                    "phenotypic_meropenem_mic",
                    "phenotypic_amikacin",
                    "phenotypic_amikacin_mic",
                    "phenotypic_streptomycin",
                    "phenotypic_streptomycin_mic",
                    "phenotypic_ethionamide",
                    "phenotypic_ethionamide_mic",
                    "phenotypic_prothionamide",
                    "phenotypic_prothionamide_mic",
                    "phenotypic_para_aminosalicylic",
                    "phenotypic_para_aminosalicylic_mic",
                    "xpert_mtb_refampicin",
                    "xpert_xdr_isoniazid",
                    "xpert_xdr_fluoroquinolones",
                    "xpert_xdr_amikacin",
                    "xpert_xdr_kanamycin",
                    "xpert_xdr_capreomycin",
                    "xpert_xdr_ethionamide",
                    "nanopore_rifampicin",
                    "nanopore_rifampicin_mic",
                    "nanopore_isoniazid",
                    "nanopore_isoniazid_mic",
                    "nanopore_levofloxacin",
                    "nanopore_levofloxacin_mic",
                    "nanopore_moxifloxacin",
                    "nanopore_moxifloxacin_mic",
                    "nanopore_bedaquiline",
                    "nanopore_bedaquiline_mic",
                    "nanopore_linezolid",
                    "nanopore_linezolid_mic",
                    "nanopore_clofazimine",
                    "nanopore_clofazimine_mic",
                    "nanopore_cycloserine",
                    "nanopore_cycloserine_mic",
                    "nanopore_terizidone",
                    "nanopore_terizidone_mic",
                    "nanopore_ethambutol",
                    "nanopore_ethambutol_mic",
                    "nanopore_delamanid",
                    "nanopore_delamanid_mic",
                    "nanopore_pyrazinamide",
                    "nanopore_pyrazinamide_mic",
                    "nanopore_imipenem_cilastatin",
                    "nanopore_imipenem_cilastatin_mic",
                    "nanopore_meropenem",
                    "nanopore_meropenem_mic",
                    "nanopore_amikacin",
                    "nanopore_amikacin_mic",
                    "nanopore_streptomycin",
                    "nanopore_streptomycin_mic",
                    "nanopore_ethionamide",
                    "nanopore_ethionamide_mic",
                    "nanopore_prothionamide",
                    "nanopore_prothionamide_mic",
                    "nanopore_para_aminosalicylic",
                    "nanopore_para_aminosalicylic_mic",
                    "genotype_mtbdrplus",
                    "genotype_mtbdrsi",
                    "nanopore_version_number",
                    "nanopore_lot_number",
                    "nanopore_resistance_detected",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "phenotypic_rifampicin",
        "phenotypic_isoniazid",
        "phenotypic_levofloxacin",
        "phenotypic_moxifloxacin",
        "created",
    )

    list_filter = (
        "report_datetime",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "phenotypic_rifampicin": admin.VERTICAL,
        "phenotypic_isoniazid": admin.VERTICAL,
        "phenotypic_levofloxacin": admin.VERTICAL,
        "phenotypic_moxifloxacin": admin.VERTICAL,
        "phenotypic_bedaquiline": admin.VERTICAL,
        "phenotypic_linezolid": admin.VERTICAL,
        "phenotypic_clofazimine": admin.VERTICAL,
        "phenotypic_cycloserine": admin.VERTICAL,
        "phenotypic_terizidone": admin.VERTICAL,
        "phenotypic_ethambutol": admin.VERTICAL,
        "phenotypic_delamanid": admin.VERTICAL,
        "phenotypic_pyrazinamide": admin.VERTICAL,
        "phenotypic_imipenem_cilastatin": admin.VERTICAL,
        "phenotypic_meropenem": admin.VERTICAL,
        "phenotypic_amikacin": admin.VERTICAL,
        "phenotypic_streptomycin": admin.VERTICAL,
        "phenotypic_ethionamide": admin.VERTICAL,
        "phenotypic_prothionamide": admin.VERTICAL,
        "phenotypic_para_aminosalicylic": admin.VERTICAL,
        "xpert_mtb_refampicin": admin.VERTICAL,
        "xpert_xdr_isoniazid": admin.VERTICAL,
        "xpert_xdr_fluoroquinolones": admin.VERTICAL,
        "xpert_xdr_amikacin": admin.VERTICAL,
        "xpert_xdr_kanamycin": admin.VERTICAL,
        "xpert_xdr_capreomycin": admin.VERTICAL,
        "xpert_xdr_ethionamide": admin.VERTICAL,
        "nanopore_rifampicin": admin.VERTICAL,
        "nanopore_isoniazid": admin.VERTICAL,
        "nanopore_levofloxacin": admin.VERTICAL,
        "nanopore_moxifloxacin": admin.VERTICAL,
        "nanopore_bedaquiline": admin.VERTICAL,
        "nanopore_linezolid": admin.VERTICAL,
        "nanopore_clofazimine": admin.VERTICAL,
        "nanopore_cycloserine": admin.VERTICAL,
        "nanopore_terizidone": admin.VERTICAL,
        "nanopore_ethambutol": admin.VERTICAL,
        "nanopore_delamanid": admin.VERTICAL,
        "nanopore_pyrazinamide": admin.VERTICAL,
        "nanopore_imipenem_cilastatin": admin.VERTICAL,
        "nanopore_meropenem": admin.VERTICAL,
        "nanopore_amikacin": admin.VERTICAL,
        "nanopore_streptomycin": admin.VERTICAL,
        "nanopore_ethionamide": admin.VERTICAL,
        "nanopore_prothionamide": admin.VERTICAL,
        "nanopore_para_aminosalicylic": admin.VERTICAL,
        "genotype_mtbdrplus": admin.VERTICAL,
        "genotype_mtbdrsi": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
