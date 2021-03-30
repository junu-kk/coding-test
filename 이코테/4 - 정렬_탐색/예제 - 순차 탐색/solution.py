from sys import stdin
input = stdin.readline


n = int(input())
arr = list(map(int, input().split()))
target = int(input())


def sequential_search(n, arr, target):
    for i in range(n):
        if arr[i] == target:
            return i+1


print(sequential_search(n, arr, target))
