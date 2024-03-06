import re

def checkPassword(password):
    reasons = []

    # Check the length of the password
    if len(password) < 8:
        reasons.append("The password is too short.")

    # Check if the password contains at least one uppercase letter
    if not re.search('[A-Z]', password):
        reasons.append("The password does not contain an uppercase letter.")

    # Check if the password contains at least one lowercase letter
    if not re.search('[a-z]', password):
        reasons.append("The password does not contain a lowercase letter.")

    # Check if the password contains at least one digit
    if not re.search('\d', password):
        reasons.append("The password does not contain a digit.")

    # Check if the password contains at least one special character
    if not re.search('[!@#$%&]', password):
        reasons.append("The password does not contain a special character.")

    if reasons:
        return False, reasons
    else:
        return True, []

# Get the password from the user
password = input("Enter a password: ")

isValid, reasons = checkPassword(password)

if isValid:
    print("Valid Password")
else:
    print("Password does not meet requirements for the following reasons:")
    for reason in reasons:
        print(reason)