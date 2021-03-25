from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for n in range(1, 21):
    print(n, is_prime(n))
