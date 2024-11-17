def deco(func):
    def wrapper(*args,**kwargs):
        print(f"Func_name:{func.__name__} and Args:{args} {kwargs}")
        res = func(*args,**kwargs)
        return res
    return wrapper

@deco
def ex_func(a,b,c):
    return a + b + c

print(ex_func(1,2,3))
print(ex_func("hello","world","!"))