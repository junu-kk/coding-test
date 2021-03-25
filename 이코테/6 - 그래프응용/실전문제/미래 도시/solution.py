from sys import stdin
input = stdin.readline
INF = int(1e9)

vn, en = map(int, input().split())
graph = [[INF]*(vn+1) for _ in range(vn+1)]
for i in range(vn+1):
    graph[i][i] = 0
for _ in range(en):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

v_start = 1
v_end, v_mid = map(int, input().split())

for v_through in range(1, vn+1):
    for v_from in range(1, vn+1):
        for v_to in range(1, vn+1):
            graph[v_from][v_to] = min(
                graph[v_from][v_to], graph[v_from][v_through]+graph[v_through][v_to])

answer = graph[v_start][v_mid] + graph[v_mid][v_end]
if answer >= INF:
    print(-1)
else:
    print(answer)
