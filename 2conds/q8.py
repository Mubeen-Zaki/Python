def password_strength(pswd):
    if len(pswd) < 6:
        print("weak")
    elif len(pswd) >= 6 and len(pswd) <= 10:
        print("strong")
    else:
        print("strong")