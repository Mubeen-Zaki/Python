import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time : {end - start}")
        return res
    return wrapper

@timer
def example(n):
    time.sleep(n)

example(5)