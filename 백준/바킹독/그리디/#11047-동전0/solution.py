coins = []
coin_n, money = map(int, input().split())
for _ in range(coin_n):
    coins.append(int(input()))

# 큰 것부터 거슬러주면 되겠다.
answer = 0
for i in range(coin_n-1, -1, -1):
    coin = coins[i]
    while money >= coin:
        money -= coin
        answer += 1
    if money == 0:
        break

print(answer)