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
class User:
    ALLOWED_ROLES = {"Doctor", "Nurse", "Biomedical Scientist", "Admin"}
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
#valid user
user1 = User("Ali", "Doctor")
#invalid user, empty name
user2 = User("", "Doctor")
#invalid user, name is a list rather than str
user3 = User(["Ali"], "Doctor") 