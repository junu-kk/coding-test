# 11 ~ 26
# 내림차순 정렬

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))


for each in sorted(arr, reverse=True):
    print(each, end=' ')
