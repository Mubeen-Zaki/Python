def sumEven(n):
    if n < 2:
        return 0
    s = 0
    # while n != 0:
    #     if n % 2 == 0:
    #         s += n
    #         n -= 2
    #     else:
    #         n -= 1
    for i in range(2, n + 1, 2):
        s += i
    return s

# print(sumEven(11))
# print(sumEven(6))

for i in range(2, 11, 2):
    print(i)