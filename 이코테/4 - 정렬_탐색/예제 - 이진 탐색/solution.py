from sys import stdin
input = stdin.readline


n = int(input())
arr = sorted(list(map(int, input().split())))  # 구현의 편의를 위해 정렬되었다고 가정함.
target = int(input())


def binary_search_iterative(arr, target, li, ri):
    while li <= ri:
        mid_i = (li+ri) // 2
        if arr[mid_i] == target:
            return mid_i
        elif arr[mid_i] > target:
            ri = mid_i - 1
        else:
            li = mid_i + 1
    return None


def binary_search_recursive(arr, target, li, ri):
    if li > ri:
        return None
    mid_i = (li+ri) // 2
    if arr[mid_i] == target:
        return mid_i
    elif arr[mid_i] > target:
        return binary_search_recursive(arr, target, li, mid_i-1)
    else:
        return binary_search_recursive(arr, target, mid_i+1, ri)


print(binary_search_iterative(arr, target, 0, n-1))
print(binary_search_recursive(arr, target, 0, n-1))
