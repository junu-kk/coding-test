from collections import deque

vn, en = map(int, input().split())
indegree = [0] * (vn+1)
graph = [[] for i in range(vn+1)]

for _ in range(en):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입차수(나에게로 향하는 엣지들 수)

def topology_sort():
    result = []
    q = deque()

    for i in range(1, vn+1): # 각 노드마다
        if indegree[i] == 0: # 진입차수 없는 것들 우선적으로
            q.append(i) # 처리큐에 넣고

    while q: # 큐 빌때까지 반복문을 돌린다.
        now = q.popleft() # 하나 꺼내
        result.append(now) # 정답에 추가하고
        for i in graph[now]: # now노드에서 뻗어나가는 엣지마다
            indegree[i] -= 1 # 없애고
            if indegree[i] == 0: # 그 엣지가 향한 노드가 외톨이가 되면
                q.append(i) # 다음에 처리하게 인큐

    for i in result:
        print(i, end=' ')

topology_sort()