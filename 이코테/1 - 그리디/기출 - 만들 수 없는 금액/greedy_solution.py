# 풀이참조 : https://hacoding.tistory.com/18

from sys import stdin
input = stdin.readline

n = int(input())
coins = sorted(list(map(int, input().split())))  # 1 1 2 3 9

answer = 1  # 1부터 만들 수 있는지 봐야하니까 1부터 시작.
for coin in coins:
    if coin <= answer:  # 동전이 해당 금액보다 작거나 같으면,
        answer += coin  # 그 사이에 있는 값들은 당연히 성립하니 더 올려준다..?
    else:
        break

print(answer)

# money_t = [False]*(sum(coins)+1)
# for pick_n in range(1, n+1):
#     for comb in combinations(coins, pick_n):
#         money_t[sum(comb)] = True

# i = 1
# for money in range(1, sum(coins)):
#     if not money_t[money]:
#         print(money)
#         break
