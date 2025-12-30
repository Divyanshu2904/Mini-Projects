import re

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = 0
    feedback = []

    #  Length
    if length >= 12:
        score += 1
    elif length >= 8:
        feedback.append("Minimum password length is 12.")

    #  uppercase and lowercase letters
    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("Mixing uppercase and lowercase letters improves security.")

    # numbers
    if has_digit:
        score += 1
    else:
        feedback.append("Including numbers will enhance security.")

    # special characters
    if has_special:
        score += 1
    else:
        feedback.append("Special characters provide better security.")

    if score >= 3:
        return "Strong password."
    else:
        return "Weak password. " + " ".join(feedback)


if __name__ == "__main__":
    print("Password Strength Checker!")
    print("Please enter your password :")

    while True:
        password = input("> ")
        if password.lower() == 'exit':
            print("Exiting...")
            break
        strength_feedback = check_password_strength(password)
        print(strength_feedback)