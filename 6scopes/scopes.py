user = "mubeen"

def func():
    user = "zaki"
    print(user)

# print(user)
# func()

x = 100

def func1():
    x = 99

def func2():
    global x
    x = 101

# func1()
# print(x)

# func2()
# print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()

# f1()

def f1():
    x = 88
    def f2():
        print(x)
    return f2

# myResult = f1()
# myResult()

#factory functions/closures
def encoder(num):
    def actual(x):
        return x ** num
    return actual

f = encoder(2)
g = encoder(3)

print(f)
print(g)

print(f(5))
print(g(6))