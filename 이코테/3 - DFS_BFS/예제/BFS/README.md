# BFS
1. 인큐 후 방문시키고
2. 다음을 반복
   1. 디큐한거 출력
   2. 인접한 아이들 방문 안했으면 인큐 후 방문


```python
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
```