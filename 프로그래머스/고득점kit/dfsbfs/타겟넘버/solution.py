answer = 0


def dfs(depth, mid_result, numbers, target):
    global answer

    if depth == len(numbers):
        if mid_result == target:
            answer += 1
        return 0

    dfs(depth + 1, mid_result + numbers[depth], numbers, target)
    dfs(depth + 1, mid_result - numbers[depth], numbers, target)


def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer

print(solution([1,1,1,1,1], 3))