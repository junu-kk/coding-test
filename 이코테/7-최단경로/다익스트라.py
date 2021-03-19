'''
최단경로 1 : 다익스트라
: from one to many, 그리디

1. 출발노드 설정
2. 최단거리테이블 초기화
반복:
    3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택 (고로 그리디.)
    (일반다익스트라는 이걸 미리 해주고, 힙다익스트라는 이것 또한 반복문 안에서 해준다.)
    
    4. 최단거리T 갱신

<추출방식 정리>
스택 : 가장 나중에 들어온 데이터 -> 파이썬 리스트로 구현 -> 삽입 추출 모두 O(1)
큐 : 가장 먼저 들어온 데이터 -> collections.deque로 구현 -> 삽입 추출 모두 O(1)
우선순위큐 : 가장 priority가 높은 데이터 -> 삽입 추출 모두 O(logn) -> 다익스트라에 사용.

'''

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def get_node():
    '''
    0순위 : (무조건) 방문 안한 노드들 중
    1순위 : 거리 짧은 노드들을 고르는데
    2순위 : 여러개면 인덱스 젤 작은거
    '''
    min_value = INF
    index = 0
    for i in range(1, vn+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):  # 간단한 형태의 다익스트라
    distance[start] = 0  # 시작점~시작점은 0이니까 0으로 찍고
    visited[start] = True  # 시작점 방문 찍고
    for adjacent in graph[start]:  # 시작점에 인접한 점들에 대해
        v, dist = adjacent
        distance[v] = dist  # 최단거리테이블에 반영

    for _ in range(vn-1):  # 시작점 0으로 세팅했으니까 나머지 vn-1번 반복 (순서대로 아님!)
        now = get_node()  # 방문 아직 안했으면서, 가장 거리가 짧은 노드를 잡아
        visited[now] = True  # 방문 찍고
        for adjacent in graph[now]:  # 인접점들에 대해
            v, dist = adjacent
            cost = distance[now] + dist  # 나를 거쳐가는 것의 코스트를 새로 계산한 다음
            if cost < distance[v]:  # 더 짧으면 갱신해줌.
                distance[v] = cost


def better_dijkstra(start):  # 우선순위큐(힙)을 사용한 조금 더 효율적인 다익스트라
    q = []  # 방문리스트 대신 힙 선언 후
    distance[start] = 0  # 시작점 0으로 찍고
    heapq.heappush(q, (0, start))  # 힙에 넣기.
    while q:  # 힙이 남아있는동안 반복
        now_dist, now_v = heapq.heappop(q)  # 하나 꺼내서(최소힙이니까 최단거리 알아서 꺼내짐)
        if distance[now_v] < now_dist:  # 최단거리T값이 단순 거리보다 작을때는 그냥 무시
            continue
        for adjacent in graph[now_v]:  # 그 그래프와 인접한 점들에 대해
            v, dist = adjacent
            cost = now_dist + dist  # 이전거리 + 지금거리 더하고
            if cost < distance[v]:  # 최단거리테이블 갱신할만하면 갱신한 뒤 heappush
                distance[v] = cost
                heapq.heappush(q, (cost, v))


vn, en = map(int, input().split())
start_v = int(input())
graph = [[] for _ in range(vn+1)]  # 다익스트라 -> 인접리스트 사용.
visited = [False] * (vn+1)  # 방문T 세팅
distance = [INF] * (vn+1)  # 최단거리T 처음엔 모두 inf로 세팅

for _ in range(en):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))

############ 둘 중에 하나 실행 고고 ################
# dijkstra(start)
# better_dijkstra(start)
###############################################

for i in range(1, vn+1):  # start에서 가는 경로 얼마나 걸리는지 출력
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])
