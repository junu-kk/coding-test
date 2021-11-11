# arr 중 두 수의 합이 k가 되는 개수
def solution(arr, k):
    answer = 0
    arr_d = dict()  # k-v : 값-인덱스
    for i in range(len(arr)):
        arr_d[arr[i]] = i

    for i in range(len(arr)):
        finding = k - arr[i]
        if finding in arr_d and arr_d[finding] != i:
            answer += 1

    return answer // 2


print(solution([1, 2, 3], 3))
