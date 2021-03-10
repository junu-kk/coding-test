# ~6
'''
input
N M
N개의떡길이들

output
절단기높이

답안을 봤는데
이진탐색을 어떻게 적용하냐면

나름 정직하게 적용함.

'''

N, M = map(int, input().split())
ddeoks = sorted(list(map(int, input().split())), reverse=True)

start = 0
end = N-1
answer = 0

while start <= end:
    ddeok_length = 0
    mid = (start+end) // 2
    for ddeok in ddeoks:
        if ddeok > mid:
            ddeok_length += x - mid
    if ddeok_length < M:
        end = mid - 1
    else:
        result = mid # ddeok_length가 M보단 크거나 같아야 하므로 여기서 기록!
        start = mid + 1

print(result)
