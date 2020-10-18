BLANK = 0
WALL = 1
VIRUS = 2

n, m = map(int, input().split())
graph = []
after_graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

'''
dfs든 bfs든 퍼지는건 쭉 계산하면 될거고..
각각 퍼질때마다 유효성검사 해서 벽에 부딪히거나 끝에 다다르면 탐색종료
그래서 0을 다 2로 만든 담에, 남아있는 0을 세면 될텐데
이 3개를 콤비네이션 써서 해보면 될것같다.

근데 진짜 감이 오지 않으므로 일단 패스.
'''

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0

def infect(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= ny < m: # 유효범위 내에서
            if after_graph[nr][nc] == BLANK: # 감염이 되지 않았다면
                after_graph[nr][nc] = VIRUS # 감염시키고
                infect(nr, nc) # 재귀적으로 감염 고고 (dfs의 원리)

def get_blankn():
    blankn = 0
    for i in range(n):
        for j in range(m):
            balnkn += 1
    return blankn

def dfs(walln):
    global answer
    if walln == 3:
        for i in range(n):
            for j in range(m):
                after_graph[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if after_graph[i][j] == VIRUS:
                    infect(i, j)
        answer = max(answer, get_blankn())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == BLANK: # 빈칸이면
                graph[i][j] == WALL # 벽세우고
                walln += 1
                dfs(walln) # 아.. 벽 3개 될때까지 재귀돌리는 거구나.. 사실 콤비네이션의 원리도 재귀여서..ㅎ
                graph[i][j] = BLANK # 다시 허물고
                walln -= 1

dfs(0)
print(answer)