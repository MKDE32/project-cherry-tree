import string



RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"



def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        strength = "Schwach"
        color = RED
    elif score <= 4:
        strength = "Mittel"
        color = YELLOW
    elif score <= 5:
        strength = "Stark"
        color = GREEN
    else:
        strength = "Sehr stark"
        color = GREEN

    return strength, score, color

password = input("Gib dein Passwort ein: ")
strength, score, color = check_password_strength(password)
print(f"Passwortstärke: {color}{strength} (Score: {score}/6)")


