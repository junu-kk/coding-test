from sys import stdin
input = stdin.readline

vn, en = map(int, input().split())
graph = [[] for _ in range(vn+1)]
for _ in range(en):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit_t = [False] * (vn+1)
visit_t2 = [False] * (vn+1)


def dfs_original(v):
    s = [v]
    visit_t2[v] = True
    while s:
        v = s.pop()
        print(v, end=' ')
        for adj_v in graph[v]:
            if not visit_t2[adj_v]:
                s.append(adj_v)
                visit_t2[adj_v] = True


def dfs(v):
    visit_t[v] = True
    print(v, end=' ')

    for adj_v in graph[v]:
        if not visit_t[adj_v]:
            dfs(adj_v)


dfs(1)
dfs_original(1)
