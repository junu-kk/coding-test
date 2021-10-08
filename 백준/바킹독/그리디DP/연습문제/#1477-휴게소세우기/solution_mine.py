'''
# io
6 7 800 // 휴개소 6개있는데 7개를 더 지을거고 고속도로길이는 800임
622 411 201 555 755 82 // 휴게소의 각 위치들

70 // 휴게소가 없는 구간의 최댓값의 최솟값

# notes
최댓값의 최솟값 하니까 21카인턴 코테 5번이 생각나네..
그리고 푸는 과정에서 네클 기출도 생각난다.
=> parametric search

힙 쓰니까 정확하지가 않게 된다. 이따가 반례 찾아보자.

# strategy


# pseudo code



'''
from heapq import heappush, heappop

n, m, l = map(int, input().split())
data = list(map(int, input().split()))
h = []  # 최대힙
prev_data = 0
for each in sorted(data):
    heappush(h, -(each - prev_data))
    prev_data = each
heappush(h, -(l - prev_data))
for _ in range(m):
    max_dist = -heappop(h)
    heappush(h, -(max_dist // 2))
    heappush(h, -(max_dist // 2) if max_dist % 2 == 0 else -((max_dist // 2) + 1))

print(-heappop(h))
