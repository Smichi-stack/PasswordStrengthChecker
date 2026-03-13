from utils import score_password

def strength(p):
    s = score_password(p)

    if s <= 1:
        return "very weak"
    if s == 2:
        return "weak"
    if s == 3:
        return "fine"
    if s == 4:
        return "strong"
    return "very strong"
