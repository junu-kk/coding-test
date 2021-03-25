from math import sqrt
from sys import stdin
input = stdin.readline

n = int(input())
prime_t = [True]*(n+1)  # 소수만 출력할거니까 0과 1은 고려 안합니다 ㅎ.

for i in range(2, int(sqrt(n))+1):
    if prime_t[i] == True:
        j = 2
        while i*j <= n:
            prime_t[i*j] = False
            j += 1

for i in range(2, n+1):
    if prime_t[i]:
        print(i, end=' ')
