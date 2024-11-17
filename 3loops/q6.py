def fact(n):
    if n == 0:
        return 0
    p = 1
    while n != 0:
        p *= n
        n -= 1
    return p

print(fact(6))