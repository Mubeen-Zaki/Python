import math
def area_circum(r):
    temp = math.pi * r
    return round(temp * r,2), round(2 * temp,2)

area, circum = area_circum(5)

print(area, circum)