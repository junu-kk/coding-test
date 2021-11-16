def dfs(v_start, graph):
    vn = len(graph)
    visit_t = [False] * vn
    visit_t[v_start] = True
    s = [v_start]

    while s:
        v = s.pop()
        print(f'{v} 방문')
        for adj_v in graph[v]:
            if not visit_t[adj_v]:
                s.append(adj_v)
                visit_t[adj_v] = True


v_start = 0
graph = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
vn = 4
visit_t = [False] * vn


def dfs_recursive(v):
    visit_t[v] = True
    print(f'{v} 방문')

    for adj_v in graph[v]:
        if not visit_t[adj_v]:
            dfs_recursive(adj_v)


dfs(0, [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]])
dfs_recursive(0)
