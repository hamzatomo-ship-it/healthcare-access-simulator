#Roles
ALLOWED_ROLES = {
    "Doctor",
    "Nurse",
    "Biomedical-Scientist",
    "Admin",
}
#catalog of available add-on
AVAILABLE_ADDONS = {
    "blood_film",
    "reticulocytes",
    "iron_studies",
}

#catalog of reason to amend on system
AMEND_REASONS = {
    "preliminary_to_final",
    "post_analytical_review",
    "sample_quality_issue",
    "instrument_error",
}

# catalog of role permissions
ROLE_PERMISSIONS = {
    "Doctor": {
        "view_demographics",
        "view_lab_results",
        "request_addon_test",
    },
    "Nurse": {
        "view_demographics",
        "view_lab_results",
    },
    "Biomedical-Scientist": {
        "view_demographics",
        "view_lab_results",
        "amend_lab_results",
        "request_addon_test",
    },
    "Admin": {
        "view_demographics",
        "view_lab_results",
    },
}

# Which add-ons each role is allowed to request
ROLE_ADDONS = {
    "Doctor": {"blood_film", "reticulocytes", "iron_studies"},
    "Biomedical-Scientist": {"blood_film"},  # only blood film
    "Nurse": set(),
    "Admin": set(),
}

# Which amend reasons each role is allowed to use
ROLE_AMEND_REASONS = {
    "Biomedical-Scientist": {
        "preliminary_to_final",
        "post_analytical_review",
        "sample_quality_issue",
        "instrument_error",
    },
    "Doctor": set(),
    "Nurse": set(),
    "Admin": set(),
}


# User Class


class User:
    def __init__(self, name: str, role: str):
        # validating user name
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")

        # validating user role
        if role not in ALLOWED_ROLES:
            raise ValueError(f"Invalid role: {role}. Allowed roles: {sorted(ALLOWED_ROLES)}")

        self.name = name
        self.role = role

    def request_addon_test(self, addon: str) -> bool:
        # 1) validate add-on exists
        if addon not in AVAILABLE_ADDONS:
            raise ValueError(f"Unknown add-on test: {addon}")

        # 2) permission gate
        if "request_addon_test" not in ROLE_PERMISSIONS.get(self.role, set()):
            raise PermissionError(f"{self.role} is not allowed to request add-on tests")

        # 3) policy gate: allowed add-ons for this role
        allowed_addons = ROLE_ADDONS.get(self.role, set())
        if addon not in allowed_addons:
            raise PermissionError(f"{self.role} cannot request: {addon}")

        return True

    def amend_lab_result(self, reason: str) -> bool:
        # 1) validate reason exists
        if reason not in AMEND_REASONS:
            raise ValueError(f"Unknown amend reason: {reason}")

        # 2) permission gate
        if "amend_lab_results" not in ROLE_PERMISSIONS.get(self.role, set()):
            raise PermissionError(f"{self.role} is not allowed to amend lab results")

        # 3) policy gate: allowed reasons for this role
        allowed_reasons = ROLE_AMEND_REASONS.get(self.role, set())
        if reason not in allowed_reasons:
            raise PermissionError(f"{self.role} cannot amend for reason: {reason}")

        return True
    
    
   # Quick Test Section 
if __name__ == "__main__":
    # Doctor tests
    user1 = User("Ali", "Doctor")
    print(user1.request_addon_test("reticulocytes"))  # True

    # # Biomedical Scientist tests
    bms = User("Sam", "Biomedical-Scientist")
    print(bms.request_addon_test("blood_film"))  # True
    print(bms.amend_lab_result("preliminary_to_final"))  # True

    # Uncomment these to confirm errors are working as expected:
    # nurse = User("Bea", "Nurse")
    # print(nurse.request_addon_test("blood_film"))  # PermissionError
    # print(bms.request_addon_test("iron_studies"))  # PermissionError
    # # print(user1.amend_lab_result("preliminary_to_final"))  # PermissionError
    # print(bms.amend_lab_result("made_up_reason"))  # ValueError
