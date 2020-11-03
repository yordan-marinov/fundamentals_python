def length_password(text: str):
    if len(text) not in range(6, 11):
        return "Password must be between 6 and 10 characters"
    return "valid"


def letters_digits_only(text: str):
    if not text.isalnum():
        return "Password must consist only of letters and digits"
    return "valid"


def at_least_2_digits(text: str):
    result = [c for c in text if c.isdigit()]
    if len(result) < 2:
        return "Password must have at least 2 digits"
    return "valid"


def password_validator(password: str):
    validation = [
        length_password(password),
        letters_digits_only(password),
        at_least_2_digits(password),
    ]
    if validation.count("valid") == len(validation):
        return "Password is valid"
    else:
        return "\n".join([i for i in validation if i != "valid"])


data = input()

print(password_validator(data))
