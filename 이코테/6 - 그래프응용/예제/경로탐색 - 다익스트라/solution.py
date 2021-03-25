from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
INF = int(1e9)

vn, en = map(int, input().split())
v_start = int(input())
graph = [[] for _ in range(vn+1)]
dist_t = [INF]*(vn+1)

for _ in range(en):
    v_from, v_to, cost = map(int, input().split())
    graph[v_from].append((v_to, cost))


def dijkstra(v_start):
    q = []
    heappush(q, (0, v_start))
    dist_t[v_start] = 0

    while q:
        dist, v = heappop(q)
        if dist <= dist_t[v]:  # 최단거리테이블 갱신각이 보일때
            for adj_v_dist in graph[v]:  # 인접노드야, 나를 거쳐가는게 빠르다면 그렇게 하렴
                adj_v, adj_dist = adj_v_dist
                dist_new = dist+adj_dist
                if dist_new < dist_t[adj_v]:
                    dist_t[adj_v] = dist_new  # 나를 거쳐가는 만큼
                    heappush(q, (dist_new, adj_v))  # 너도 언젠가는 다리가 되렴.


dijkstra(v_start)
for dist in dist_t[1:]:
    print(dist)
