# 그리디 거스름돈 문제 매운맛

n, m = map(int, input().split()) # m원을 효율적으로 구성하는 것이 목표.
coins = []
for i in range(n):
    coins.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if d[j-coins[i]] != 10001: # 코인 하나만 더 쓰면 지불할 수 있는 상황이라면
            d[j] = min(d[j], d[j-coins[i]] + 1) # 기존값 유지(이미 방법이 나와있을 수 있으니 ㅇㅇ) vs 코인 하나 더 쓰기

if d[m] == 10001:
    print(-1)
else:
    print(d[m])