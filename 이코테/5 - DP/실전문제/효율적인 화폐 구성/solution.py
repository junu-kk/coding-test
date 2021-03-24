from sys import stdin
input = stdin.readline

coin_n, n = map(int, input().rstrip().split())
dp_t = [-1]*1001
coins = []
for _ in range(coin_n):
    coin = int(input())
    coins.append(coin)
    dp_t[coin] = 1

for i in range(1, n+1):
    possible_vs = []
    for coin in coins:
        if dp_t[i-coin] > 0:
            possible_vs.append(dp_t[i-coin]+1)
    if len(possible_vs) > 0:
        dp_t[i] = min(possible_vs)

print(dp_t[n])
