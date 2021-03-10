import heapq

n, m = map(int, input().split())
table = [1e9] * (n+1)
graph = [[] for _ in range(n+1)]    # 그래프에 엣지 저장시 번호만 저장

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

table[1] = 0
q = []
heapq.heappush(q, (0, 1))
while q:
    dist, v = heapq.heappop(q)
    for node in graph[v]:
        if table[node] <= dist:
            continue
        table[node] = min(table[node], dist+1)
        heapq.heappush(q, (table[node], node))

result = table[1]
cnt = 1
idx = 1
for i in range(2, n+1):
    if result < table[i]:
        idx = i
        result = table[i]
        cnt = 1
    elif result == table[i]:
        cnt += 1

# 변수명 중복해서 짓지 말기
print(idx, result, cnt)
