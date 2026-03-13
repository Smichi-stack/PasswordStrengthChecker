from utils import score_password

def strength(p):
    s = score_password(p)

    if s <= 1:
        return "Very Weak"
    if s == 2:
        return "Weak"
    if s == 3:
        return "Fine"
    if s == 4:
        return "Strong"
    return "Very Strong"
