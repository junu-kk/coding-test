'''
좌표 압축 기법을 적용해야 한다고 함.



'''
from itertools import combinations

rn, cn = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(rn)]
answer = 0
for row1, row2 in combinations(mtrx, 2):
    # print(row1, row2)
    for i, j in combinations(list(range(cn)), 2):
        # print(i, j)
        a1, a2, b1, b2 = row1[i], row1[j], row2[i], row2[j]
        # print(a1, a2, b1, b2)
        if not ((a1 < a2 and b1 < b2) or (a1 > a2 and b1 > b2) or (a1 == a2 and b1 == b2)):
            break
    else:
        answer += 1

print(answer)
