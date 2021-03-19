N = int(input())
coins = [500, 100, 50, 10]
answer = 0

for coin in coins:
    coin_n = N // coin
    answer += coin_n
    N -= coin*coin_n

print(answer)
