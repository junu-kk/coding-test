def solution(array:list, cmds:list):
    answer = []
    for start_o, end_o, big_o in cmds:
        v = sorted(array[start_o-1:end_o])[big_o-1]
        answer.append(v)

    return answer

print(solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))