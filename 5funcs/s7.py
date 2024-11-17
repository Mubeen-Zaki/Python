def sum(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum(1,2,3))
print(sum(1,2,3,4,5))