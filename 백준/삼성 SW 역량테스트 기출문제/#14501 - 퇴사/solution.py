'''
<느낀 점>
1. dp테이블이 순차적으로 세워나가기 좀 어려울 때는, reverse 아이디어도 한 번 적용해보자.
2. dp테이블로 모든 걸 해결하지 말고, (인덱스로 참조만 할 수 있도록) 다른 테이블들도 적극 활용하자.

summary
생략

input
7 : 7일동안 최대한 이익이 되는 방향으로 상담을 하려 한다.
3 10 : 1일차에 잡힌 상담은 3일이 걸리고, 보수는 10이다.
5 20 : 2일차에 잡힌 상담은 5일이 걸리고, 보수는 20이다.
1 10 : ...
1 20
2 15
4 40 : 6일차에 잡힌 상담은 4일이 걸리고, 보수는 40이다.
2 200 : 7일차에 잡힌 상담은 2일이 걸리고, 보수는 200이다.

output
45 : 적절히 취사선택 했을 때 얻을 수 있는 최대 이익은 45이다.

strategy
dp로 일단 풀어야겠다는건 알겠다.
1일차까지,사
2일차까지,
...
7일차까지.

종이에 그려봐도 도통 접근을 어떻게 해야 할지 모르겠어서 나동빈 교재 참조함.

'''
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
