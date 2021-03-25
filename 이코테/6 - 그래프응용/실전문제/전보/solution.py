from sys import stdin
input = stdin.readline

INF = int(1e9)

vn = int(input())
en = int(input())
graph = [[INF]*(vn+1) for _ in range(vn+1)]

for i in range(1, vn+1):
    graph[i][i] = 0

for _ in range(en):
    v_from, v_to, cost = map(int, input().split())
    graph[v_from][v_to] = cost

for v_through in range(1, vn+1):
    for v_from in range(1, vn+1):
        for v_to in range(1, vn+1):
            graph[v_from][v_to] = min(
                graph[v_from][v_to], graph[v_from][v_through] + graph[v_through][v_to])


for v_from in range(1, vn+1):
    for v_to in range(1, vn+1):
        dist = graph[v_from][v_to]
        if dist == INF:
            print('x', end=' ')
        else:
            print(dist, end=' ')
    print()
