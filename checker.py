from utils import score_password

def strength(p):
    s = score_password(p)
    if s <= 2:
        return "Weak"
    if s == 3:
        return "Medium"
    return "Strong"
