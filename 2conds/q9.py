def isLeapYear(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

assert isLeapYear(2000) == True
assert isLeapYear(1600) == True
assert isLeapYear(2400) == True


