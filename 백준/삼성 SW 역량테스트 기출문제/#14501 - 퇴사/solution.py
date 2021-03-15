from sys import stdin
input = stdin.readline

n = int(input())
times = []  # 상담을 완료하는데 걸리는 기간
prices = []  # 상담을 완료했을 때 받을 수 있는 금액
dp_t = [0] * (n+1)
max_profit = 0

for _ in range(n):
    time, price = map(int, input().split())
    times.append(time)
    prices.append(price)

for i in range(n-1, -1, -1):
    end_time = times[i] + i
    if end_time <= n:  # 기간 안에 상담 종료
        dp_t = max(prices[i]+dp_t[time], max_profit)
        max_profit = dp_t[i]
    else:  # 기간 넘어가면 이뤄질 수 없으니 변화 X
        dp_t[i] = max_profit
