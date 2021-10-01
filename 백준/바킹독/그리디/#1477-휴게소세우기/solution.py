'''
# io
6 7 800 // 휴개소 6개있는데 7개를 더 지을거고 고속도로길이는 800임
622 411 201 555 755 82 // 휴게소의 각 위치들

70 // 휴게소가 없는 구간의 최댓값의 최솟값

# notes
최댓값의 최솟값 하니까 21카인턴 코테 5번이 생각나네..
=> parametric search



# strategy


# pseudo code



'''
n, m, l = map(int, input().split())
data = list(map(int, input().split()))

data.append(0)
data.append(l-1)
data.sort()

start = (0)
end = data[-1]
while start <= end:
    cnt = 0
    mid = (start+end) // 2
    for i in range(1, len(data)):
        chai = data[i] - data[i-1]
        if chai > mid:
            cnt += (chai-1) // mid

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)
