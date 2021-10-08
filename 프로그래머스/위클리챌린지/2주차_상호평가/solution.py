'''
# io


# notes
서로가 서로를 평가해 평균을 냄.
자기자신을 평가한 점수가 유일한 최고 or 최저면 제외함.
2명 이상.

# strategy
힙 쓰면 편하겠다.
자기가 최고점이면서 최저점일 수 있나?
그럴 수 있다.


# pseudo code
'''
from heapq import heappush, heappop


def get_lettergrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    n = len(scores)
    answer = []
    for i in range(n):
        minh = []
        maxh = []
        exclude_min, exclude_max = False, False
        score_sum = 0
        bunmo = n
        for x in range(n):
            score = scores[x][i]
            heappush(minh, (score, x))
            heappush(maxh, (-score, x))
            score_sum += score

        v1, i1 = heappop(minh)
        v2, i2 = heappop(minh)
        if v1 != v2 and i1 == i:  # 값이 다르고 최솟값의 주인이 자기 자신일경우
            exclude_min = True

        v3, i3 = heappop(maxh)
        v4, i4 = heappop(maxh)
        v3, v4 = -v3, -v4
        if v3 != v4 and i3 == i:  # 값이 다르고 최댓값의 주인이 자기 자신일경우
            exclude_max = True

        if exclude_min and exclude_max and i1 == i3:
            score_sum -= v1
            bunmo -= 1
        else:
            if exclude_min:
                score_sum -= v1
                bunmo -= 1
            if exclude_max:
                score_sum -= v3
                bunmo -= 1

        result = score_sum / bunmo
        answer.append(get_lettergrade(result))

    return ''.join(answer)