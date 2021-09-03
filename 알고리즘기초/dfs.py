vn, en = map(int, input().split())
es = []
for _ in range(en):
    es.append(list(map(int, input().split())))

graph = [[] for _ in range(vn+1)]


for e in es:
    v1, v2 = e
    graph[v1].append(v2)


s = [1]
visit_t = [False] * (vn+1)
visit_t[1] = True

while s:
    v = s.pop()
    print(v, end=' ')
    for adj_v in graph[v]:
        if not visit_t[adj_v]:
            s.append(adj_v)
            visit_t[adj_v] = True

