from heapq import heappush, heappop, heapify


def solution(scoville: list, k: int):
    answer = 0
    heapify(scoville)
    while len(scoville) > 1:
        f1 = heappop(scoville)
        f2 = heappop(scoville)
        if f1 >= k:
            return answer
        newf = f1 + f2 * 2 if f1 < f2 else f2 + f1 * 2
        heappush(scoville, newf)
        answer += 1

    if scoville[0] >= k:
        return answer

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
