def age_group(n):
    if n < 0 or n > 150:
        return "Enter valid age"
    if n < 13:
        return "child"
    elif n >= 13 and n <= 19:
        return "teen"
    elif n > 19 and n < 60:
        return "adult"
    else:
        return "senior citizen"

age = int(input("Enter age : "))
print(age_group(age))