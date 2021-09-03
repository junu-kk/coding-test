from itertools import product

def solution(numbers, target):
    n = len(numbers)
    depth = 0
    s = [numbers[0]]
    mid_result = 0
    answer = 0
    while s:
        if depth == n and mid_result == target:
            answer += 1

        num = s.pop()
        for op in ('+', '-'):
            if op == '+':
                mid_result += num
                s.append(numbers[depth+1])
            elif op == '-':
                mid_result -= num
                s.append(numbers[depth+1])
        depth += 1


    return answer


print(solution([1,1,1,1,1], 3))