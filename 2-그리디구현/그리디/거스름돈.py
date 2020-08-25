# 500 100 50 10 많이 있을때
# n원을 거슬러 줘야할때
# 거슬러줄수있는 최소 동전의 수

n = int(input())
coins = (500,100,50,10)
answer = 0
for coin in coins:
    coin_n = n // coin # 동전개수
    answer += coin_n
    n -= coin * coin_n
print(answer)