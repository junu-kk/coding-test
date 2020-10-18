from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

'''
이 그래프를 갖고 뭘 해야 하느냐.
x에서 k만큼 떨어진 도시를 모두 출력하고
만약 없으면 -1 출력하면 됨.

... 이게 bfs인 이유는
나도 잘 모르겠다.
dfs로 풀어보면 안되나?
dfs로 해도 될것같은데?

'''
distance = [-1] * (n+1) # 방문리스트를 원래는 True / False로 했었는데 거리로 하는거면 -1부터 출발해도 됨ㅇㅇㅇ.
distance[x] = 0 # 일단 첫번째 노드 방문하고
def solution_bfs():
    q = deque([x]) # 첫번째 노드 큐에 넣은담에
    while q: # bfs 돌리기
        now = q.popleft() # 하나 꺼내서
        for visiting in graph[now]: # 인접한 노드들한테
            if distance[visiting] == -1: # 방문을 안했다면 방문처리
                distance[visiting] = distance[now] + 1
                q.append(visiting) # 담에 방문할 수 있도록 인큐까지!

    visit = False
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            visit = True

    if not visit:
        print(-1)



solution_bfs()