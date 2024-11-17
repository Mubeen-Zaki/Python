from datetime import datetime

def movie_ticket_price(age, day):
    p1 = 12
    p2 = 8
    if day == 'wednesday':
        p1 -= 2
        p2 -= 2
    if age >= 18:
        return p1
    else:
        return p2

age = int(input("Enter age:"))
day = datetime.now().strftime('%A')
# print(day)
print(movie_ticket_price(age, 'wednesday'))