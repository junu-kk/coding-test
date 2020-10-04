import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def get_smallest_node(): # 아직 방문하지 않는 노드 중 최단거리T 최솟값 인덱스 찾아 리턴
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]: # 최단거리테이블의 값이 최소이면서 아직 방문 안한 상태이면 고고.
            min_value = distance[i]
            index = i
    return index

def dijkstra(start): # 간단한 형태의 다익스트라
    distance[start]=0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost<distance[j[0]]:
                distance[j[0]] = cost

def better_dijkstra(start): # 힙을 사용한 조금 더 효율적인 다익스트라
    q = [] # 힙 선언 후
    heapq.heappush(q, (0, start)) # 시작부분 heappush
    distance[start] = 0
    while q: # 힙이 남아있는동안 반복
        dist, now = heapq.heappop(q) # 하나 꺼내서(힙이니까 최단거리 알아서 꺼내짐)
        if distance[now] < dist: # 최단거리T값이 단순 거리보다 작을때는 그냥 무시
            continue
        for i in graph[now]: # 그 그래프와 인접한 점들에 대해
            cost = dist + i[1] # 이전거리 + 지금거리 더하고
            if cost < distance[i[0]]: # 최단거리테이블 갱신할만하면 갱신한 뒤 heappush
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1) # 방문T 세팅
distance = [INF] * (n+1) # 최단거리T 처음엔 모두 inf로 세팅

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 둘 중에 하나 실행 고고
# dijkstra(start)
# better_dijkstra(start)

for i in range(1, n+1): # start에서 가는 경로 얼마나 걸리는지 출력
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])