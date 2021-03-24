from sys import stdin
input = stdin.readline

n = int(input())
dp_t = [0]*n
dp_t[0], dp_t[1] = 1, 3


for i in range(2, n):
    dp_t[i] = (dp_t[i-2]*2+dp_t[i-1]) % 796796

print(dp_t[n-1])
