from sys import stdin
input = stdin.readline

'''
1. dp_t를 적당히 잡고
2. dp_t 초기값을 잡고
3. 규칙성을 찾아서 쭈루루룩
'''

n = int(input().rstrip())
days_costs = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
dp_t = [0]*(n+1)  # 0~n-1로 적용할 예정이지만, 마지막날을 위해 한칸 더 선언


for i in range(n-1, -1, -1):  # 거꾸로 계산
    day, cost = days_costs[i]
    if i + day > n:  # 기한 안에 못할 일이면 스킵
        dp_t[i] = dp_t[i+1]  # 아....
        continue

    dp_t[i] = max(dp_t[i+1], dp_t[i+day] + cost)

print(dp_t[0])
