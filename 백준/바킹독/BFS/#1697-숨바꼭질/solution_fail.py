'''
dp인가?

5 17
5 10 9 18 17
4

전혀 bfs가 아닌 것 같은 때에 bfs가 쓰일 수 있다는 점을 명심하자.
약간 bfs를 이용한.. dp느낌도 나고...
생각해보니 둘이 좀 통하는것같다.
'''
from collections import deque

UNVISITED = -1
depth_t = [UNVISITED] * 100002
start, end = map(int, input().split())

q = deque([start])
depth_t[start] = 0
while q:
    loc = q.popleft()

    if loc == end:
        print(depth_t[loc])
        exit(0)

    for nxt in (loc-1, loc+1, loc*2):
        if not (0<=nxt<100000):
            continue
        if depth_t[nxt] != UNVISITED:
            continue

        depth_t[nxt] = depth_t[loc] + 1


print(depth_t[end])
