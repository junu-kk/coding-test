def solution(dist, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(dist)

    l, r = 0, dist

    while l <= r:
        # mid : 거리의 최솟값을 뜻함.
        mid = (l+r) // 2

        # 각 mid 설정에서의 최소 거리
        min_dist = dist
        cur_loc = 0
        rmv_n = 0

        for rock in rocks:
            tmp_dist = rock - cur_loc
            # 현 거리가 mid보다 가깝다면 돌 없애고
            if tmp_dist < mid:
                rmv_n += 1
            # mid보다 멀다면 최소거리 변경
            else:
                cur_loc = rock
                min_dist = min(min_dist, tmp_dist)

        # 더 많이 없앴다면 반영 X
        if rmv_n > n:
            r = mid - 1
        else:
            answer = min_dist
            l = mid + 1

    return answer




    return answer


print(solution(25, [2,14,11,21,17], 2))