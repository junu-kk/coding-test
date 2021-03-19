# DFS

## 오리지날
1. 푸시 후 방문시키고
2. 다음을 반복
   1. 팝한거 출력
   2. 인접한 아이들 방문 안했으면 푸시 후 방문

## 재귀 이용
1. 방문 후 출력
2. 인접한 아이들 방문 안했으면 dfs

```python
def dfs_original(v):
    s = [v]
    visit_t[v] = True
    while s:
        v = s.pop()
        print(v, end=' ')
        for adj_v in graph[v]:
            if not visit_t[adj_v]:
                s.append(adj_v)
                visit_t[adj_v] = True


def dfs(v):
    visit_t[v] = True
    print(v, end=' ')

    for adj_v in graph[v]:
        if not visit_t[adj_v]:
            dfs(adj_v)
```