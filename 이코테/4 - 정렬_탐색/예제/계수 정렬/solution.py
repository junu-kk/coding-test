from sys import stdin
input = stdin.readline


n = int(input())
arr = list(map(int, input().split()))  # 0 이상만 들어온다고 가정.

counts = [0]*(max(arr)+1)

for i in range(n):
    counts[arr[i]] += 1

for i in range(n):
    for j in range(counts[i]):
        print(i, end=' ')
