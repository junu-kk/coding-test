INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1): # 그래프 000 세팅
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m): # 그래프 나머지값들 세팅
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, n+1): # 삼중반복문 돌리면서
    for a in range(1, n+1): # 직빵으로 가기 vs 거쳐가기 중 빠른 걸 택해
        for b in range(1, n+1): # 그래프에 넣어줍니다
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1): # 결과출력
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('infinity', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()