from math import sqrt
from sys import stdin
input = stdin.readline

l, r = map(int, input().split())
prime_t = [True for _ in range(1000001)]
prime_t[1] = False

for i in range(2, int(sqrt(r))+1):
    if prime_t[i]:
        j = 2
        while i*j <= r:
            prime_t[i*j] = False
            j += 1

for i in range(l, r+1):
    if prime_t[i]:
        print(i)
