INF = int(1e9)

vn, en = map(int, input().split())
graph = [[INF] * (vn+1) for _ in range(vn+1)] # 일단 무한대로 초기화

for a in range(1, vn+1): # 자기자신 0으로 초기화
    for b in range(1, vn+1):
        graph[a][b] = 0

for _ in range(en): # lower -> higher를 1로 줌.
    lower, higher = map(int, input().split())
    graph[lower][higher] = 1

for mid in range(1, en+1): # 이제 플로이드 워셜을 돌릴건데
    for low in range(1, en+1): # 0과 1과 INF밖에 없으니
        for high in range(1, en+1): # 간접적인 서열도 나올거임.
            graph[low][high] = min(graph[low][high], graph[low][mid] + graph[mid][high])

result = 0 # 자기 순위가 정해진 사람들 수
for i in range(vn+1): # 사람 i와
    count = 0
    for j in range(1, vn+1): # 사람 j가
        if not (graph[i][j] == INF and graph[j][i] == INF): # 뭔가 서열관계가 정해져 있다면
            count += 1 # 카운트 하나 늘리고
    if count == vn: # 만약 그 카운트가 맥스이면 다른 사람들과 다 비교가 된다는 뜻이고 이는 본인의 순위를 정할 수 있다는 뜻이므로
        result += 1 # 하나 플러스

print(result)