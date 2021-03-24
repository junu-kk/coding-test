from sys import stdin
input = stdin.readline

n = int(input())
foods = list(map(int, input().split()))
dp_t = [0]*n
dp_t[0] = foods[0]
dp_t[1] = max(foods[0], foods[1])
for i in range(n):
    dp_t[i] = max(dp_t[i-1], dp_t[i-2]+foods[i])

print(dp_t[n-1])
