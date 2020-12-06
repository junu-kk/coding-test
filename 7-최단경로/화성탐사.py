import heapq
INF = int(1e9)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

tcn = int(input())

def main(): # 다익스트라 너무 어렵다. 플로이드 와샬은 쉬운데
    vn = int(input())
    graph = []
    for i in range(vn): # 그래프에 일단 고대로 추가
        graph.append(list(map(int, input().split()))) 
    
    distance = [[INF] * vn for _ in range(vn)]

    r, c = 0, 0
    q = [(graph[r][c], r, c)] # 비용과 좌표 일단 0,0에있는거 넣고
    distance[r][c] = graph[r][c] # 디스턴스 또한 그래프 고대로 가져감

    while q: # 이제 큐를 계속 돌리면서
        dist, r, c = heapq.heappop(q)
        if distance[r][c] < dist: # 처리된적 있는 노드면 넘어가고
            continue
        for i in range(4): # 4방향 모두 움직여가며
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= vn or nc < 0 or nc >= vn: # 범위 벗어나면 나가리
                continue
            cost = dist + graph[nr][nc] # 비용 함 업데이트 해주고
            if cost < distance[nr][nc]: # 나쁘지 않은 선택이라면 힙에 추가
                distance[nr][nc] = cost
                heapq.heappush(q, (cost, nr, nc))
    
    return distance[nr-1][nc-1] # 그래서 끝까지 갔을 때 최소를 출력

for tc in range(tcn):
    print(main())