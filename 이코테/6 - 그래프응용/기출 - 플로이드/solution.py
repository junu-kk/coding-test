from sys import stdin
input = stdin.readline
INF = int(1e9)

vn = int(input().rstrip())
en = int(input().rstrip())
graph = [[INF]*(vn+1) for _ in range(vn+1)]
for v in range(1, vn+1):
    graph[v][v] = 0

for _ in range(en):
    v_from, v_to, cost = map(int, input().rstrip().split())
    graph[v_from][v_to] = min(graph[v_from][v_to], cost)

for v_through in range(1, vn+1):
    for v_from in range(1, vn+1):
        for v_to in range(1, vn+1):
            graph[v_from][v_to] = min(
                graph[v_from][v_to], graph[v_from][v_through]+graph[v_through][v_to])

for r in range(1, vn+1):
    for c in range(1, vn+1):
        if graph[r][c] >= INF:
            print(0, end=' ')
        else:
            print(graph[r][c], end=' ')
    print()
