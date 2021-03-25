from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
INF = int(1e9)

vn, en, v_from = map(int, input().split())
graph = [[] for _ in range(vn+1)]
dist_t = [INF] * (vn+1)
for _ in range(en):
    v_from, v_to, cost = map(int, input().split())
    graph[v_from].append((v_to, cost))

q = []
heappush(q, (0, v_from))
dist_t[v_from] = 0
while q:
    dist, v = heappop(q)
    if dist_t[v] < dist:
        continue
    for adj_v_cost in graph[v]:
        adj_v, adj_cost = adj_v_cost
        dist_new = dist + adj_cost
        if dist_t[adj_v] > dist_new:
            dist_t[adj_v] = dist_new
            heappush(q, (adj_cost, adj_v))

availalbe_vn = 0
max_dist = -INF
for v in range(1, vn+1):
    if dist_t[v] < INF:
        availalbe_vn += 1
        max_dist = max(max_dist, dist_t[v])

print(availalbe_vn-1, max_dist)
