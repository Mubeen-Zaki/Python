def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int( n ** 0.5)):
        if n % i == 0:
            return False
    return True

print(isPrime(18))
print(isPrime(23))