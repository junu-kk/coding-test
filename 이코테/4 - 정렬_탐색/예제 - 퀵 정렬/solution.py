from sys import stdin
input = stdin.readline


n = int(input())
arr = list(map(int, input().split()))


def quick_sort_py(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    list_except_pivot = arr[1:]

    list_under_pivot = [x for x in list_except_pivot if x <= pivot]
    list_over_pivot = [x for x in list_except_pivot if x > pivot]

    return quick_sort_py(list_under_pivot) + [pivot] + quick_sort_py(list_over_pivot)


def quick_sort(arr, start_i, end_i):
    if start_i >= end_i:
        return

    pi, li, ri = start_i, start_i+1, end_i
    while li <= ri:
        while li <= end_i and arr[li] <= arr[pi]:
            li += 1
        while ri > start_i and arr[ri] >= arr[pi]:
            ri -= 1
        if li > ri:  # 엇갈렸다면 더 작은 값은 ri가 갖고 있을 거임.
            arr[ri], arr[pi] = arr[pi], arr[ri]
        else:
            arr[li], arr[ri] = arr[ri], arr[li]

    quick_sort(arr, start_i, ri-1)
    quick_sort(arr, ri+1, end_i)


quick_sort(arr, 0, n-1)
print(arr)
