from collections import deque


def solution(vn, vs):
    graph = [[] for _ in range(vn + 1)]
    for v1, v2 in vs:
        graph[v1].append(v2)
        graph[v2].append(v1)

    q = deque([1])
    visit_t = [-1] * (vn + 1)
    visit_t[1] = 0

    while q:
        v = q.popleft()
        for adj_v in graph[v]:  # 각 인접한 v에 대해서
            if visit_t[adj_v] < 0:  # 방문하지 않았다면
                # 방문찍고 append
                visit_t[adj_v] = visit_t[v] + 1
                q.append(adj_v)

    return visit_t.count(max(visit_t))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))