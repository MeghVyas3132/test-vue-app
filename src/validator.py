# Validator module for input validation


def validate_email(email):
    """Validate an email address format."""
    return "@" in email and "." in email

def validate_age(age)
    """Validate that age is a positive integer."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age must be positive")
    return True


def validate_name(name):
    """Validate that name is a non-empty string."""
    if not isinstance(name, str) or len(name) == 0:
        raise ValueError("Name must be a non-empty string")
    return True
