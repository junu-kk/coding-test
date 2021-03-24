from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
arr_a = sorted(list(map(int, input().split())))
arr_b = sorted(list(map(int, input().split())), reverse=True)
answer = 0
j = 0

for i in range(n):
    if i < k:
        if arr_a[i] > arr_b[j]:
            answer += arr_a[i]
        else:
            answer += arr_b[j]
            j += 1
    else:
        answer += arr_a[i]

print(answer)
