from itertools import combinations
from sys import stdin
input = stdin.readline

n = int(input())
coins = list(map(int, input().split()))

money_t = [False]*(sum(coins)+1)
for pick_n in range(1, n+1):
    for comb in combinations(coins, pick_n):
        money_t[sum(comb)] = True

i = 1
for money in range(1, sum(coins)):
    if not money_t[money]:
        print(money)
        break
