'''
<io>
5
4 1 5 2 3 # 이 수들이 풀이고
5
1 3 7 9 5 # 각 수들이 위 집단에 존재하는가?

1
1
0
0
1

<notes>
존재하면 1, 존재하지 않으면 0

<strategy>
그냥 set 쓰면 되지 않음? O(n)에 해결될텐데
그래도 한 번 이분탐색으로 해보자.

'''

n = int(input())
pool = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

def bs(num):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r) // 2
        if pool[mid] == num:
            return 1
        elif pool[mid] >= num:
            r = mid - 1
        else:
            l = mid + 1
    return 0

for num in nums:
    print(bs(num))
