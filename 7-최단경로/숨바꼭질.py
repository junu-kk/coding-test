import heapq
INF = int(1e9)

n, m = map(int, input().split()) # v개수, e개수
start = 1

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m): # e 입력받기
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # 거리 / v
    graph[b].append((a, 1))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start)) # (0, 1) 먼저 넣고
    distance[start] = 0 # 거리테이블 초기화한다음에
    while q:
        dist, now = heapq.heappop(q) # 거리 / v 꺼내서 
        if distance[now] < dist: # 이미 최단거리가 나와있다면.. 그냥 스킵
            continue
            
        for i in graph[now]: # 그 v와 연결된 모든 e에 대해
            cost = dist + i[1] # cost는 이번 v를 거쳐갈 때의 비용.
            if cost < distance[i[0]]: # 만약 최단거리가 나왔다면
                distance[i[0]] = cost # 최단거리테이블 바꿔주고
                heapq.heappush(q, (cost, i[0])) # 푸시해주면 됨.

dijkstra(start)

max_node = 0 # 제일 먼 곳
max_distance = 0 # 제일 멀리도망갈수있는
result = [] # 쌤쌤노드 모음

for i in range(1, n+1):
    if max_distance < distance[i]: # 최단거리가 나타났다면
        max_node = i # 갱신
        max_distance = distance[i] # 갱신
        result = [max_node] # 갱신
    elif max_distance == distance[i]: # 쌤쌤이면
        result.append(i) # 하나만 더해줌

print(max_node, max_distance, len(result))