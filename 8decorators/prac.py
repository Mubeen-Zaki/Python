# Create a decorator called `retry` that will retry a function up to 3 times if it raises an exception. If the function succeeds, it should return the result, but if it fails after 3 attempts, it should print an error message.

def retry(func):
    def wrapper(*args,**kwargs):
        c = 0
        while c < 3:
            try:
                res = func(*args,**kwargs)
            except Exception as e:
                c += 1
                continue
            else:
                print("successful")
                return res
        return "unsuccessful"
    return wrapper

@retry
def divide(a,b):
    res = a / b
    return res

print(divide(3,0))
print(divide(3,3))