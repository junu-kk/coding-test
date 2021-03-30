from sys import stdin
input = stdin.readline


n = int(input())
arr = list(map(int, input().split()))


def insertion_sort(n):
    for i in range(1, n):  # 오른쪽 정렬안된부분 맨 앞을 골라
        for j in range(i, 0, -1):  # 왼쪽 정렬된 부분에
            if arr[j-1] > arr[j]:  # 삽입한다 == 오른쪽에서 왼쪽으로 swap해나간다.
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:  # 제자리를 찾으면 break
                break


insertion_sort(n)
print(arr)
