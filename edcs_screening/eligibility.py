from django.utils.safestring import mark_safe

from edcs_constants.constants import (
    CANCER_FREE,
    LUNG_CANCER_SUSPECT,
    NO,
    OTHER_CANCER,
    TBD,
    YES,
)
from edcs_utils.date import get_utcnow


class SubjectScreeningEligibilityError(Exception):
    pass


class EligibilityPartOneError(Exception):
    pass


class EligibilityPartTwoError(Exception):
    pass


class EligibilityPartThreeError(Exception):
    pass


def check_eligible_final(obj):
    """Updates model instance fields `eligible` and `reasons_ineligible`."""
    reasons_ineligible = []

    if obj.patient_18yrs == NO:
        obj.eligible = False
    elif obj.symptoms_pulmonary == NO:
        obj.eligible = False
    elif obj.respiratory_sample == NO:
        obj.eligible = False
    elif obj.consent == NO:
        obj.eligible = False
    else:
        obj.eligible = True if calculate_eligible_final(obj) == YES else False

    if obj.eligible:
        obj.reasons_ineligible = None
    else:
        if obj.patient_18yrs == NO:
            reasons_ineligible.append("Patient is not least 18 years old")
        if obj.symptoms_pulmonary == NO:
            reasons_ineligible.append(
                "Patient is not presented with signs and symptoms suggestive"
                " of pulmonary TB or another pulmonary infection of "
                "bacterial, viral, or fungal origin")
        if obj.respiratory_sample == NO:
            reasons_ineligible.append("Patient is not capable of producing a respiratory "
                                      "sample")
        if obj.consent == NO:
            reasons_ineligible.append("Patient is not will to provided written consent to "
                                      "participate")
        if reasons_ineligible:
            obj.reasons_ineligible = "|".join(reasons_ineligible)
        else:
            obj.reasons_ineligible = None
    obj.eligibility_datetime = get_utcnow()


def calculate_eligible_final(obj):
    """Returns YES, NO or TBD."""
    if (
        obj.patient_18yrs in [YES, NO]
        and obj.symptoms_pulmonary in [YES, NO]
        and obj.respiratory_sample in [YES, NO]
        and obj.consent in [YES, NO]
    ):
        eligible = (
            # obj.abnormal_chest_xrays == YES
            # or obj.non_resolving_infection == YES
            # or obj.lung_cancer_suspect == YES
            # or obj.cough == YES
            # or obj.long_standing_cough == YES
            # or obj.cough_blood == YES
            # or obj.chest_infections == YES
            obj.patient_18yrs == YES and obj.consent == YES
            and (obj.symptoms_pulmonary == YES and obj.respiratory_sample == YES)
        )
        return NO if not eligible else YES
    return TBD


def format_reasons_ineligible(*str_values):
    reasons = None
    str_values = [x for x in str_values if x is not None]
    if str_values:
        str_values = "".join(str_values)
        reasons = mark_safe(str_values.replace("|", "<BR>"))
    return reasons


def eligibility_display_label(obj):
    if obj.eligible:
        display_label = "ELIGIBLE"
    elif calculate_eligible_final == TBD:
        display_label = "PENDING"
    else:
        display_label = "Not eligible"
    return display_label
