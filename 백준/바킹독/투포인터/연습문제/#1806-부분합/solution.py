'''
<io>
10 15 # 크기 10짜리, 합은 15 이상이어야 함.
5 1 3 5 10 7 4 9 2 8 # 수열
5 6 9 14 24
2 # 합이 15 이상 되는 연속된 수들의 부분합 중 가장 짧은 길이는 {10,7}로 길이 2

<notes>
불가능하다면 0 출력

<strategy>
5 1 3 5
'''
from sys import maxsize as INF

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = INF

# prefix sum 해야하나? ㅇㅇ 그러면 되겠다.
pfx_sum_t = [0] * (n + 1)
pfx_sum_t[0] = 0
for i in range(1, n + 1):
    pfx_sum_t[i] = pfx_sum_t[i - 1] + nums[i - 1]

l, r = 0, 1
while l < n+1 and r < n+1:
    hap = pfx_sum_t[r] - pfx_sum_t[l]
    if hap >= m:
        answer = min(answer, r - l)
        l += 1
    else:
        r += 1

print(0 if answer == INF else answer)
