import heapq
import sys
INF = int(1e9)

vn, en, start_v = map(int, input().split())
graph = [[] for _ in range(vn+1)]
distance = [INF] * (vn+1)

for _ in range(en):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for injeop in graph[now]:
            cost = dist + injeop[1]
            if cost < distance[injeop[0]]:
                distance[injeop[0]] = cost
                heapq.heappush(q, (cost, injeop[0]))

dijkstra(start_v) # 다익스트라 적용 후

count = 0
max_distance = 0
for dist in distance:
    if dist != INF: # 갈 수 있는 경우
        count += 1 # 노드하나 추가요
        max_distance = max(max_distance, dist) # 최대거리 갱신

print(count-1, max_distance)