INF = int(1e9)

vn = int(input())
en = int(input())

graph = [[INF]*(vn+1) for _ in range(vn+1)] # 그래프 초기화

for a in range(vn+1): # 자기자신으로 가는거 0으로 초기화
    for b in range(1, vn+1):
        if a == b:
            graph[a][b] = 0

for _ in range(en):
    start, end, cost = map(int, input().split())
    if cost < graph[start][end]: # 짧은 경우에만 저장.
        graph[start][end] = cost

for mid in range(1, n+1): # 플로이드 워셜 고고
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

for a in range(1, n+1): # 출력부분
    for b in range(1, n+1):
        if graph[a][b] == INF: # 도달할수없는경우
            print(0, end=' ')
        else: # 도달할수있는경우
            print(graph[a][b], end=' ')
    print()
