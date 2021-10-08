def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

begin, end = map(int, input().split())
prime_t = [True] * 1000001
prime_t[1] = False
for i in range(2, int(1000000**0.5) + 1):
    if prime_t[i] and is_prime(i):
        j = 2
        while i*j <= 1000000:
            prime_t[i*j] = False
            j += 1


for num in range(begin, end+1):
    if prime_t[num]:
        print(num)