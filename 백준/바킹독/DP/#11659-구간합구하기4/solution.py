'''
# io
5 3 # 수는 5개, 구해야할 구간합은 3개
5 4 3 2 1 # nums
1 3 # 순서
2 4
5 5

12
9
1

# notes


# strategy
구간 합 문제이다.
미리 누적합을 구해놓은 다음에
1 3이면 pfx_sum[3] - pfx_sum[0] 해주면 되겠다.

# pseudo code



'''
import sys

input = sys.stdin.readline


num_n, ggh_n = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

# 구간합 구해놓고
pfx_sum = [0] * (num_n+1)
for i in range(1, num_n+1):
    pfx_sum[i] = nums[i-1] + pfx_sum[i-1]

for _ in range(ggh_n):
    a, b = map(int, input().rstrip().split())
    print(pfx_sum[b] - pfx_sum[a-1])