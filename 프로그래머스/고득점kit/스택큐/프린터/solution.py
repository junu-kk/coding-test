from heapq import heappop, heappush
from collections import deque


def solution(priorities: list, location: int):
    h = []
    idx_pri_q = deque(enumerate(priorities))
    for pri in priorities:
        heappush(h, -pri)

    print_count = 0
    pri_to_print = -heappop(h)
    while idx_pri_q:
        idx, pri = idx_pri_q.popleft()
        if pri == pri_to_print:
            print_count += 1
            if idx == location:
                return print_count
            pri_to_print = -heappop(h)
        else:
            idx_pri_q.append((idx, pri))

    return 0


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
