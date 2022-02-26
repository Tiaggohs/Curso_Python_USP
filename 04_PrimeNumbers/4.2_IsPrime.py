def isPrime(n):
    d = 2
    prime = True

    while (prime and d < n):
        rest = n % d
        d = d + 1
        if (rest == 0):
            prime = False

    return prime
        
def maior_primo(x):
    p = False
    while (p == False):
        if (isPrime(x)):
            p = True
        else:
            x = x - 1

    return x

