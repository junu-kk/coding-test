'''
# io
5
6 3 2 10 -10 # 이 안에서
8
10 9 -5 2 3 4 5 -10 # 이 숫자들이 들어있는지, 아닌지 구하기


# notes
그냥 이분탐색으로 하라는 뜻이다.

# strategy


# pseudo code



'''
from bisect import bisect_left as bl, bisect_right as br

_ = int(input())
nums = sorted(map(int, input().split()))
__ = int(input())
find_bys = list(map(int, input().split()))


def bs(num):
    if br(nums, num) == bl(nums, num):
        return 0
    return 1


def bs2(l, r, num):
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == num:
            return 1
        elif nums[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return 0


for each in find_bys:
    # print(bs(each), end=' ')
    print(bs2(0, _ - 1, each), end=' ')
