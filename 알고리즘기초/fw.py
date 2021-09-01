'''
fw : 그래프에서 최단경로 찾기.
인접행렬 사용함.

놓친부분 : 대각선 0 초기화, through start end의 순서.
'''

vn, en = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(vn+1) for _ in range(vn+1)]
for v in range(vn+1):
    graph[v][v] = 0

for _ in range(en):
    v1, v2, cost = map(int, input().split())
    graph[v1][v2] = cost



for v_through in range(1, vn+1):
    for v_start in range(1, vn+1):
        for v_end in range(1, vn+1):
            graph[v_start][v_end] = min(graph[v_start][v_end], graph[v_start][v_through] + graph[v_through][v_end])

print(graph)
