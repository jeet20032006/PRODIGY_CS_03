import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters.")

    # Feedback message
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

# Example usage:
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions to improve:")
    for tip in feedback:
        print(f"- {tip}")
