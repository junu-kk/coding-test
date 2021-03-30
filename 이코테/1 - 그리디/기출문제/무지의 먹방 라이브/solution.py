def solution(foods, k):
    food_n = len(foods)
    i = 0
    time_elapsed = 0
    while time_elapsed < k:
        if i == food_n:
            if sum(foods) == 0:
                return -1
            i = 0
        if foods[i] > 0:
            foods[i] -= 1
            time_elapsed += 1
        i += 1

    for _ in range(food_n):
        if i == food_n:
            i = 0
        if foods[i] > 0:
            return i+1
        i += 1
    return -1


print(solution([3, 1, 2], 5))
