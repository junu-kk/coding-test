'''
<io>
5 # 개수
2 # 집합
3
5
10
18

18 # 3수의 합이 그 안에 있어야 함.

<notes>
일단 답은 무조건 집합 안에 있어야 할거고..
그러면 큰거 -> 작은거 순으로 되는지 알아보면 되겠네.

<strategy>
nums를 역순정렬해서 받은 다음에
i는 0부터 3개남기는 (n-4)까지 iterate 하면 될거고.
합이 nums[i] 될 때의 후보군으로는 nums[i+1:]중에서 3개 뽑으면 될 것임.

'''

from itertools import combinations
n = int(input())
nums = sorted([int(input()) for _ in range(n)], reverse=True)
for i in range(n-3):
    hubo = nums[i]
    for comb in combinations(nums[i+1:], 3):
        if hubo == sum(comb):
            print(hubo)
            exit()


