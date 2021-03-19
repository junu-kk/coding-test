from collections import deque

# 준비물 1 : 그래프
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 준비물 2 : 방문리스트
dfs_visited = [False] * 9
bfs_visited = [False] * 9


# 준비물 3 : 함수
# 인자는 준비물 두 개와 방문점 or 시작점
def dfs(graph, v, visited):
    # 방문 후
    visited[v] = True
    print(v, end=' ')

    # 해당 점과 연결된 v들에 대해 방문 안되어있으면 dfs
    # 애초에 재귀함수 구조가 스택이니~~
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v_start, visited):
    # queue init : 첫 점 방문대기등록
    # 큐는 약간 예비방문대기줄 느낌. 방문리스트랑 헷갈리지 말자!
    q = deque([v_start])
    visited[v_start] = True
    
    while q:
        # 디큐하며 방문인증 하고
        v = q.popleft()
        print(v, end=' ')

        # 해당 점과 연결된 v들에 대해 방문 안되어있으면 방문대기등록
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, 1, dfs_visited)
bfs(graph, 1, bfs_visited)