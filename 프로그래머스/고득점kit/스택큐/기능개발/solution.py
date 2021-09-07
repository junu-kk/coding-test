from math import ceil
from collections import deque


def get_baepo_day(progress, speed):
    return ceil((100 - progress) / speed)


def solution(progresses: list, speeds: list):
    n = len(progresses)
    baepo_days = deque()
    for progress, speed in zip(progresses, speeds):
        baepo_day = get_baepo_day(progress, speed)
        baepo_days.append(baepo_day)
    # print(baepo_days)

    answer = []
    gijun = baepo_days.popleft()
    baepo_count = 1
    while baepo_days:
        baepo_day = baepo_days.popleft()
        if gijun < baepo_day:
            # answer 어펜드 처리
            answer.append(baepo_count)
            baepo_count = 1
            gijun = baepo_day
        else:
            # 적립처리
            baepo_count += 1

    answer.append(baepo_count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
