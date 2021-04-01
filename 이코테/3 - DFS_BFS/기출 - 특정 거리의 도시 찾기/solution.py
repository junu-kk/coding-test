from collections import deque
from sys import stdin
input = stdin.readline

vn, en, dist, v_start = map(int, input().split())
depth_t = [-1]*(vn+1)
graph = [[] for _ in range(vn+1)]
for _ in range(en):
    v_from, v_to = map(int, input().split())
    graph[v_from].append(v_to)

depth_t[v_start] = 0
q = deque([v_start])
while q:  # depth를 어떻게 구하지?
    v = q.popleft()
    for adj_v in graph[v]:
        if depth_t[adj_v] == -1:
            depth_t[adj_v] = depth_t[v] + 1
            q.append(adj_v)

v_found = False
for v in range(vn+1):
    if depth_t[v] == dist:
        v_found = True
        print(v)
if not v_found:
    print(-1)
