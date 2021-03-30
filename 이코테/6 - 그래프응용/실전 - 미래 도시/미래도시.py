# 진짜 코드만 알고 있으면 풀 수 있다.
# 플로이드워셜을 써야겠다! 라고 느낌을 잡는 게 중요한듯.

INF = int(1e9)

vn, en = map(int, input().split())
graph = [[INF] * (vn+1) for _ in range(vn+1)]

for a in range(1, vn+1):
    for b in range(1, vn+1):
        if a == b:
            graph[a][b] = 0

for _ in range(en): # 가중치 없는 그래프이므로 바로 입력받아서 1로 만들어버리기
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

to, via = map(int, input().split()) # to랑 via 헷갈릴뻔!

for k in range(1, vn+1):
    for a in range(1, vn+1):
        for b in range(1, vn+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
print(graph)
answer = graph[1][via] + graph[via][to]

if answer >= INF:
    print(-1)
else:
    print(answer)
            