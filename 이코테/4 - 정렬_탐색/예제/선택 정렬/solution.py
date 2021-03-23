from sys import stdin
input = stdin.readline


n = int(input())
arr = list(map(int, input().split()))


def selection_sort(n):
    for i in range(n):  # i : 오른쪽 정렬안된부분의 맨 앞
        minv_i = i  # minv_i : 오른쪽 정렬안된부분의 가장 작은 값의 인덱스
        for j in range(i+1, n):  # j는 오른쪽 정렬안된부분을 훑는 인덱스
            if arr[minv_i] > arr[j]:
                minv_i = j
        arr[i], arr[minv_i] = arr[minv_i], arr[i]  # 스왑


selection_sort(n)
print(arr)
