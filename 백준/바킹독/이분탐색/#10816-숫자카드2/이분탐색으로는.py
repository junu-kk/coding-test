'''
<io>
10 # 숫자카드 풀
6 3 2 10 10 10 -10 -10 7 3
8 # 각각 몇개인지 구해야함
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2

<notes>
이것도.. 이분탐색 대신 카운터로 하면 쉽게 풀릴것인데
이분탐색 한다면 bl, br 써야겠다.
<strategy>

'''
from bisect import bisect_left as bl, bisect_right as br

n = int(input())
pool = sorted(list(map(int, input().split())))
m = int(input())
answer = []
nums = list(map(int, input().split()))
for num in nums:
    answer.append(br(pool, num) - bl(pool, num))

print(*answer)
