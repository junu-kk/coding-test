'''
<io>
10 # 숫자카드 풀
6 3 2 10 10 10 -10 -10 7 3
8 # 각각 몇개인지 구해야함
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2

<notes>
이것도.. 이분탐색 대신 카운터로 하면 쉽게 풀릴것인데

<strategy>

'''
from collections import Counter

n = int(input())
counter_d = Counter(map(int, input().split()))
m = int(input())
answer = [0] * m
nums = list(map(int, input().split()))
for i in range(m):
    num = nums[i]
    if num in counter_d:
        answer[i] = counter_d[num]

print(*answer)