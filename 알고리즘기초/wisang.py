'''
큐 썼던거랑, indegree 썼던거 말고는 기억이 하나도 안난다.
다시 치면서 다음엔 안보고 칠 수 있게 해보자.

- indegree 테이블 만들고
- graph 만들어 하나씩 넣어주고
- indegree 0인것부터 큐에 넣어주고
- while q 돌리면서, 하나씩 빼서 v_orders에 넣어주고
- 인접점에 대해 반복 돌리면서, indegree 하나씩 빼주고 0이되는거 있음 큐에 삽입
(0이되는게 두개가 된다? 그럼 순서보장이 안되는 거라고 할 수 있겠지.)
'''

from collections import deque

vn, en = map(int, input().split())
graph = [[] for _ in range(vn+1)]
indegree_t = [0] * (vn+1)

for _ in range(en):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    indegree_t[v2] += 1


def topology_sort():
    v_orders = []
    q = deque()

    for v in range(1, vn+1):
        if indegree_t == 0:
            q.append(v)

    while q:
        v = q.popleft()
        v_orders.append(v)
        for adj_v in graph[v]:
            indegree_t[adj_v] -= 1
            if indegree_t[adj_v] == 0:
                q.append(adj_v)


topology_sort()