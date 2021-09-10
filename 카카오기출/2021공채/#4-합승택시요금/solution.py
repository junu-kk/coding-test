'''
<io>
vn
v_start
v_end1
v_end2
es (v_from, v_to, cost)
result 최저 예상 택시요금은?

<notes>
무방향 가중치

<strategy>
다익스트라로 v_start에서 다른 곳으로 가는 최단거리는 구할 수 있음.
만약 v_start~v_end1, v_start~v_end2를 구하면서
경로를 저장해두고
겹치는 경로에 대해서만 한 번 계산해주면 되지 않을까?
(완벽한 풀이는 아닌것같음)

경로를 어떻게 저장하는지만 학습하면 되겠다.

플로이드와샬로 전체 최단거리를 구할 수 있음.



'''

from heapq import heappush, heappop

INF = int(1e9)


def dijkstra(dist_t, v_start, graph):
    h = []
    heappush(h, (0, v_start))
    dist_t[v_start] = 0
    while h:
        dist, v = heappop(h)
        if dist_t[v] < dist:
            continue
        for adj_v, adj_cost in graph[v]:
            new_dist = dist + adj_cost
            if new_dist < dist_t[adj_v]:
                dist_t[adj_v] = new_dist
                heappush(h, (new_dist, adj_v))


def solution(vn, v_start, v_end1, v_end2, es):
    graph = [[] for _ in range(vn + 1)]
    for v_from, v_to, cost in es:
        graph[v_from].append((v_to, cost))
        graph[v_to].append((v_from, cost))

    dist_t = [INF] * (vn + 1)
    dijkstra(dist_t, v_start, graph)
    answer = INF
    # 여기까진 일반적인 다익스트라.
    # 구한 dist_t의 v는 환승 지점이 된다.
    # .. 걍 fw 써도 될것같은데? 아 근데 효율 생각하면 다익스트라가 낫다고 한다.
    for v in range(1, vn + 1):
        tdt = [INF] * (vn + 1)
        dijkstra(tdt, v, graph)
        result = dist_t[v] + tdt[v_end1] + tdt[v_end2]
        answer = min(answer, result)
    return answer

