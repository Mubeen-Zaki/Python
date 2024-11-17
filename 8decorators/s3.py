import time

def cache(func):
    cache_value = dict()
    def wrapper(*args):
        if args in cache_value:
            print("Args in cache detected!")
            return cache_value[args]
        res = func(*args)
        cache_value[args] = res
        return res
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(4)
    return a + b

print(long_running_func(3,4))
print(long_running_func(3,4))
print(long_running_func(2,3))
print(long_running_func(3,4))
print(long_running_func(2,3))
print(long_running_func(2,33))