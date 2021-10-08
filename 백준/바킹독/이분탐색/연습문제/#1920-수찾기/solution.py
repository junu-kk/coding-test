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

'''

n = int(input())
s = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
for num in nums:
    print(1 if num in s else 0)