from collections import deque
from sys import stdin
input = stdin.readline

vn, en = map(int, input().split())
graph = [[] for _ in range(vn+1)]
indegree_t = [0]*(vn+1)
for _ in range(en):
    v_from, v_to = map(int, input().split())
    graph[v_from].append(v_to)
    indegree_t[v_to] += 1

q = deque([])
for v in range(1, vn+1):
    if indegree_t[v] == 0:
        q.append(v)

while q:
    v = q.popleft()
    print(v, end=' ')
    for adj_v in graph[v]:
        indegree_t[adj_v] -= 1
        if indegree_t[adj_v] == 0:
            q.append(adj_v)
