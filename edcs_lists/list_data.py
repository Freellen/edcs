from edcs_constants.constants import (
    NEVER,
    NONE,
    NONE_OF_ABOVE,
    NOT_APPLICABLE,
    OTHER,
    YES_CURRENT_CHEW,
    YES_CURRENT_SMOKER,
    YES_PAST_CHEW,
    YES_PAST_SMOKER,
)

list_data = {
    "edcs_lists.infotbdxmade": [
        ("chronic_cough", "Chronic cough "),
        ("haemoptysis", "Haemoptysis"),
        ("chest_xray", "Chest X-ray abnormal, suggestive of TB"),
        ("contact_tb_patient", "Contact history with infectious TB patient"),
        ("weight_loss", "Weight loss or failure to gain weight "),
        ("unexplained_fever", "Unexplained fever"),
        ("night_sweats", "Drenching night sweats"),
        ("lymphnodes", "Swelling cervical lymphnodes"),
        (OTHER, "Other"),
    ],
    "edcs_lists.otherdxmade": [
        ("chronic_cough", "Non-tuberculous mycobacteria"),
        ("haemoptysis", "COVID-19"),
        ("chest_xray", "Bacterial pneumonia"),
        ("contact_tb_patient", "Silicosis"),
        ("weight_loss", "Asbestosis"),
        (OTHER, "Other"),
    ],
}

# preload_data = PreloadData(list_data=list_data)
