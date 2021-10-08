'''
<io>
5
2 4 -10 4 -9

2 3 0 3 1

<notes>
"나보다 작은 좌표 수"

<strategy>
BST가 딱 떠오르면서 bl, br 적용해야겠다는 생각이 든다.
정렬한담에 그냥 bl 혹은 br값이 답인것같은데
1. pool에 중복제거 해줘야 하고
2. 더 작은 것들을 찾아야 하는거니 bl로 해주면 되겠다.
'''
from bisect import bisect_right as br, bisect_left as bl

n = int(input())
nums = list(map(int, input().split()))
pool = sorted(list(set(nums)))
for num in nums:
    print(bl(pool, num), end=' ')
