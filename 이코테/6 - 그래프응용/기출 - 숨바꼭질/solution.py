from collections import deque
from sys import stdin
INF = int(1e9)
input = stdin.readline

vn, en = map(int, input().rstrip().split())
graph = [[] for _ in range(vn+1)]
for _ in range(en):
    v1, v2 = map(int, input().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

depth_t = [-1]*(vn+1)
q = deque([1])
depth_t[1] = 0
while q:
    v = q.popleft()
    for adj_v in graph[v]:
        if depth_t[adj_v] == -1:
            q.append(adj_v)
            depth_t[adj_v] = depth_t[v] + 1
# print(depth_t)
max_depth = max(depth_t)
answer_v = depth_t.index(max_depth)
max_count = depth_t.count(max_depth)

print(answer_v, max_depth, max_count)
# from heapq import heappush, heappop
# from sys import stdin
# INF = int(1e9)
# input = stdin.readline

# vn, en = map(int, input().rstrip().split())
# graph = [[] for _ in range(vn+1)]
# for _ in range(en):
#     v1, v2 = map(int, input().rstrip().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# dist_t = [INF]*(vn+1)

# dist_t[1] = 0
# q = [1]

# while q:
#     v = heappop(q)
#     for adj_v in graph[v]:
#         dist_t[adj_v]
