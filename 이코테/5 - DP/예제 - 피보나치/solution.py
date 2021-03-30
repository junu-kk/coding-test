from sys import stdin
input = stdin.readline

n = int(input())
dp_t = [0]*(n+1)

dp_t[1], dp_t[2] = 1, 1

for i in range(3, n+1):
    dp_t[i] = dp_t[i-1] + dp_t[i-2]

print(dp_t[n])
