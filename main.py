ALLOWED_ROLES = {
    "Doctor",
    "Nurse",
    "Biomedical-Scientist",
    "Admin"
}

ROLE_PERMISSIONS = {
    "Doctor": {
        "view_demographics",
        "view_lab_results",
        "request_addon_test"
    },
    "Nurse": {
        "view_demographics",
        "view_lab_results"
    },
    "Biomedical-Scientist": {
        "view_demographics",
        "view_lab_results",
        "amend_lab_results"
    },
    "Admin": {
        "view_demographics",
        "view_lab_results"
    }
}
