'''
# io
10
2 -5 2 3 -4 7 -4 0 1 -6


# notes
3개합이 0이 되는 개수는?

# strategy
bf로 하면 세상 쉬운 문제
중복된 실력이 있을 수 있고 당연히 다른 경우로 간주함.

일단 정렬을 해볼까? 아!
컴비네이션 2개로 미리 합을 구해놓고 (합, i1, i2)
있는지 확인만 쏙쏙 해주면 되겠네!
근데 인덱스 세개가 겹치면 안되는 것에만 유의하자.w


# 틀렸다
시간초과도 아니고 메모리 초과...ㅋㅋ
해설 보며 다시 해보자.
=> 아이디어는 전체적으로 비슷했고,


'''
from collections import defaultdict as dd
from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
nums_d = dd(list)  # 값: [인덱스1, 인덱스2, ...]
for i in range(n):
    num = nums[i]
    nums_d[num].append(i)

answer_set = set()
for i1, i2 in combinations(list(range(n)), 2):
    hap = nums[i1] + nums[i2]
    if (-hap in nums_d) and (i1 not in nums_d[-hap]) and (i2 not in nums_d[-hap]):
        for i3 in nums_d[-hap]:
            sorted_chr_is = map(str, sorted([i1, i2, i3]))
            answer_set.add('.'.join(sorted_chr_is))

print(len(answer_set))
