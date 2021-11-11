# arr 부분배열 중 합이 k인 부분배열의 개수
def solution_bf(arr, k):
    n = len(arr)
    answer = 0
    for size in range(1, n + 1):
        i = 0
        while i <= n - size:
            if sum(arr[i:i + size]) == k:
                answer += 1
            i += 1

    return answer


# 정렬되어있을 경우 누적합 풀이 가능할듯!
def solution_eff(arr, k):
    pass




print(solution_bf([1, 2, 3], 3))
