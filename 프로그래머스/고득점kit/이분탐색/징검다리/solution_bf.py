from itertools import combinations
def solution(dist, rocks, rmv_n):
    answer = 0

    rock_n = len(rocks) + 2
    left_rock_n = rock_n-rmv_n

    rocks += [0, dist]

    for comb in combinations(rocks, left_rock_n):
        mid_answer = dist
        left_sorted_rocks = sorted(comb)
        for i in range(left_rock_n-1):
            mid_answer = min(left_sorted_rocks[i+1] - left_sorted_rocks[i], mid_answer)
    answer = max(answer, mid_answer)

    return answer


print(solution(25, [2,14,11,21,17],2))