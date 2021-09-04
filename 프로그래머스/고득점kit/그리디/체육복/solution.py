def solution(n: int, lost: list, reserve: list):
    lost_set = set(lost)
    reserve_set = set(reserve)
    to_remove = []

    for reserve in reserve_set:
        if reserve in lost_set:
            to_remove.append(reserve)
            lost_set.remove(reserve)

    for each in to_remove:
        reserve_set.remove(each)


    for reserve in reserve_set:
        if reserve - 1 in lost_set:
            lost_set.remove(reserve - 1)
        elif reserve + 1 in lost_set:
            lost_set.remove(reserve + 1)

    return n - len(lost_set)


print(solution(5, [2, 4], [1, 3, 5]))
