# 아직 이해가 완벽하게 되지 않음!
n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0] # 시작점
end = array[-1] - array[0] # 끝점
result = 0

while(start <= end): # 쭉 반복
    mid = (start+end) // 2
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)