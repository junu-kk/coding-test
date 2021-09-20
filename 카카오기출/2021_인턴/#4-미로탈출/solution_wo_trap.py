'''
<io>
vn
v_start
v_end
es
trap_vs

result

<notes>
다익스트라 복습할겸 ^^.

'''
from heapq import heappush, heappop
def solution(vn, v_start, v_end, es, trap_vs):
    graph = [[] for _ in range(vn+1)]

    for from_v, to_v, cost in es:
        graph[from_v].append((to_v, cost))

    INF = int(1e9)
    dist_t = [INF] * (vn+1)

    dist_t[v_start] = 0
    h = [(0, v_start)]

    while h:
        dist, v = heappop(h)
        if dist <= dist_t[v]:
            for adj_v, adj_dist in graph[v]:
                new_dist = dist + adj_dist
                if dist_t[adj_v] < new_dist:
                    dist_t[adj_v] = new_dist
                    heappush(h, (new_dist, adj_v))

    return dist_t[v_end]


print(solution())