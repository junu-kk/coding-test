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
nums를 정렬해서 받은 담에
i는 끝에서 3까지 내려오면 될 거고
문제는 nums[:i]에서 hubo가 되는 합이 있는지 찾아내는 일인데
prefix sum으로 접근해야 하나?
가령 1 2 4 8이 있고 11이 되는지 찾고 싶은 상황이라면..
음 모르겠다.

<해답을 보니>
미리 두수의 합을 만들어놓으면 된다고 함.
반례로 다음이 있음.
1 1 10 12

'''

from itertools import combinations_with_replacement as cwr

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
sum2_set = set()
for comb in cwr(nums, 2):
    sum2_set.add(sum(comb))

for i in range(n-1, -1, -1):
    hubo = nums[i]
    for j in range(i):
        if hubo - nums[j] in sum2_set:
            print(hubo)
            exit()



