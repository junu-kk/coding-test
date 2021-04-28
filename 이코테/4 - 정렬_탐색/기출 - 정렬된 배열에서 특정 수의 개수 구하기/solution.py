from bisect import bisect_left as bl, bisect_right as br

n, x = map(int, input().split())
nums = list(map(int, input().split()))

answer = br(nums, x)-bl(nums, x)
if answer == 0:
    print(-1)
else:
    print(answer)
