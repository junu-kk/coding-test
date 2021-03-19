from collections import deque
from sys import stdin
input = stdin.readline

vn, en = map(int, input().split())
graph = [[] for _ in range(vn+1)]
for _ in range(en):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit_t = [False] * (vn+1)


def bfs(v):
    q = deque([v])
    visit_t[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for adj_v in graph[v]:
            if not visit_t[adj_v]:
                q.append(adj_v)
                visit_t[adj_v] = True


bfs(1)
