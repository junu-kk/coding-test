'''


'''

import heapq


def solution(jobs):
    answer = 0
    heap = []

    for (start, work) in jobs:
        heapq.heappush(heap, [work, start])

    total_time, end_time = 0, 0
    while heap:
        (running_time, in_time) = heapq.heappop(heap)
        end_time += running_time

        total_time += end_time - in_time

    return total_time // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
