# test if n is prime
def isprime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

# tests each element of an array if it is prime
def f(x):
    return map(isprime,x) 