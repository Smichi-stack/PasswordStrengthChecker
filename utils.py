import re

def score_password(p):
    s = 0
    if len(p) >= 16:
        s += 1
    if re.search(r"[A-Z]", p) and re.search(r"[a-z]", p):
        s += 1
    if len(re.findall(r"[0-9]", p)) >= 2:
        s += 1
    if len(re.findall(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\];']", p)) >= 2:
        s += 1
    if len(set(p)) >= 10:
        s += 1
    if not re.search(r"(.)\1\1", p):
        s += 1
    if not re.search(r"(012|123|234|345|456|567|678|789)", p):
        s += 1
    return s