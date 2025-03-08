import re

def is_valid_email(email):
    """Check if the email format is valid (with a bug)."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.(com|com\.+[a-zA-Z]+)$'
    return re.match(pattern, email) is not None

def is_valid_password(password):
    """Check if the password is valid."""
    if not (8 <= len(password) <= 24):
        return False
    if not any(c.isupper() for c in password):  
        return False
    if not any(c.isdigit() for c in password): 
        return False
    return True  

def register(email, password, retype_password):
    """Check the input for the registration function."""
    if not is_valid_email(email):
        return "Invalid email"
    if not is_valid_password(password):
        return "Invalid password"
    if password != retype_password:
        return "Password mismatch"
    return "Success"

# Test cases for black box testing
test_cases_1 = [
    ("user1@gmail.com", "Pass123", "Pass123", "Invalid password"),
    ("user2@gmail.com", "pass123", "pass123", "Invalid password"),
    ("user3@gmail.com", "Password", "Password", "Invalid password"),
    ("user4@gmail.com", "Pass123!", "Pass123!", "Invalid password"),
    ("user5@gmail.com", "Pass1234", "Pass1243", "Password mismatch"),
    ("user1@gmail.com", "Pass1234", "Pass1234", "Success"),
    ("test123@gmail.com", "StrongPass1", "StrongPass1", "Success"),
    ("hello.world@gmail.com", "Hello1234", "Hello1234", "Success"),
    ("email_test@gmail.com", "ValidPass9", "ValidPass9", "Success"),
    ("example@gmail.com", "Example123", "Example123", "Success"),
    ("user1@yahoo.com", "Pass1234", "Pass1234", "Invalid email"),
    ("user1@gmail", "Pass1234", "Pass1234", "Invalid email"),
    ("user1@outlook.com", "Pass1234", "Pass1234", "Invalid email"),
    ("user1.gmail.com", "Pass1234", "Pass1234", "Invalid email"),
    ("user1@gmail..com", "Pass1234", "Pass1234", "Invalid email"),
    ("@gmail.com", "Pass1234", "Pass1234", "Invalid email"),
    ("user1@.com", "Pass1234", "Pass1234", "Invalid email"),
    ("user1@com", "Pass1234", "Pass1234", "Invalid email"),
    ("valid@gmail.com", "short1", "short1", "Invalid password"),
    ("valid@gmail.com", "NOLOWERCASE123", "NOLOWERCASE123", "Invalid password"),
    ("valid@gmail.com", "nouppercase123", "nouppercase123", "Invalid password"),
    ("valid@gmail.com", "NoNumberPass", "NoNumberPass", "Invalid password"),
    ("valid@gmail.com", "PassWordWith#", "PassWordWith#", "Invalid password"),
    ("valid@gmail.com", "thispasswordiswaytoolong123456", "thispasswordiswaytoolong123456", "Invalid password"),
    ("valid@gmail.com", "CorrectPass1", "WrongPass1", "Password mismatch"),
    ("valid@gmail.com", "Mismatch123", "Mismatch321", "Password mismatch"),
    ("valid@gmail.com", "UpperCaseMatch1", "uppercaseMATCH1", "Password mismatch"),
    ("valid@gmail.com", "SamePassword1", "samepassword1", "Password mismatch"),
    ("edgecase@gmail.com", "A1b23456", "A1b23456", "Success"),
    ("edgecase@gmail.com", "A1b234567890123456789012", "A1b234567890123456789012", "Success"),
    ("edgecase@gmail.com", "A1b2345", "A1b2345", "Invalid password"),
    ("edgecase@gmail.com", "A1b2345678901234567890123", "A1b2345678901234567890123", "Invalid password"),
    ("valid.email@gmail.com", "MixItUp987", "MixItUp987", "Success"),
    ("randomtest1@gmail.com", "P4sswordA", "P4sswordA", "Success"),
    ("randomtest2@gmail.com", "Qwerty123", "Qwerty123", "Success"),
    ("randomtest3@gmail.com", "A1b2C3d4", "A1b2C3d4", "Success"),
]

# Test cases for white box testing
test_cases_2 = [
    ("user@example.com", "Password123", "Password123", "Invalid email"),
    ("user@gmail.com", "Pass123", "Pass123", "Invalid password"),
    ("user@gmail.com", "password123", "password123", "Invalid password"),
    ("user@gmail.com", "Password", "Password", "Invalid password"),
    ("user@gmail.com", "Password123", "Password132", "Password mismatch"),
    ("user@gmail.com", "Password123", "Password123", "Success"),
]

for i, (email, password, confirm, expected) in enumerate(test_cases_2, 1):
    actual = register(email, password, confirm)
    result = "✅ Pass" if actual == expected else f"❌ Fail (Expected: {expected}, Got: {actual})"
    print(f"Test case {i}: {result}")
