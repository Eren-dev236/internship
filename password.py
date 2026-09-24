import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\];'`~]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Classify password
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print("-", item)
    else:
        print("✓ Your password meets all the basic security requirements!")


# Get password from user
password = input("Enter your password: ")

check_password_strength(password)