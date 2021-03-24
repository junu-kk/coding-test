# from sys import stdin
# input = stdin.readline

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))

n = 10
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

###### 1. 내장 라이브러리 사용하기 ######
# print(sorted(arr))

# 2. 선택정렬 사용하기 ###### -> 외우기 성공


def selection_sort(n, arr):
    for i in range(n):
        min_i = i
        for j in range(i, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[min_i], arr[i] = arr[i], arr[min_i]
    return arr


# print(selection_sort(n, arr))


# 3. 삽입정렬 사용하기 ###### -> 외우기 성공

def insertion_sort(n, arr):
    for i in range(1, n):  # 정렬 안된거를
        for j in range(i-1, -1, -1):  # 정렬 된쪽에 끼워넣을건데
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    return arr


# print(insertion_sort(n, arr))


# 4. 퀵정렬 사용하기 ###### -> 외우기 실패 ㅋ
# def quick_sort(n, arr, start_i, end_i):
#     if start_i > end_i:
#         return
#     pi, li, ri = start_i, start_i+1, end_i
#     while li <= ri:
#         while arr[pi] > arr[li] and li <= end_i:
#             li += 1
#         if arr[pi] > arr[ri] and ri >= start_i:
#             ri -= 1
#     pass

def quick_sort(arr, start_i, end_i):
    if start_i >= end_i:
        return

    pi, li, ri = start_i, start_i+1, end_i

    while li <= ri:
        while li <= end_i and arr[li] <= arr[pi]:
            li += 1
        while ri > start_i and arr[ri] >= arr[pi]:
            ri -= 1

        if li <= ri:  # 정상적인 경우
            arr[li], arr[ri] = arr[ri], arr[li]
        else:  # 엇갈린 경우
            arr[pi], arr[ri] = arr[ri], arr[pi]

    quick_sort(arr, start_i, ri-1)
    quick_sort(arr, ri+1, end_i)


# print(arr)
# quick_sort(arr, 0, n-1)
# print(arr)

###### 5. 계수정렬 사용하기 ######


def count_sort(arr):
    counts = [0]*(max(arr)+1)
    for i in arr:
        counts[i] += 1
    for i in range(len(counts)):
        for _ in range(counts[i]):
            print(i, end=' ')


count_sort(arr)
