BLANK = 0
WALL = 1
VIRUS = 2

n, m = map(int, input().split())
graph = []
after_graph = [[BLANK] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = 0

def infect(r, c):
    for i in range(4):
        newr = r + dr[i]
        newc = c + dc[i]
        if 0 <= newr < n and 0 <= newc < m:
            if after_graph[newr][newc] == BLANK:
                after_graph[newr][newc] = VIRUS
                infect(newr, newc)

def get_blankn():
    blankn = 0
    for i in range(n):
        for j in range(m):
            if after_graph[i][j] == BLANK:
                blankn += 1
    return blankn

def dfs(walln):
    global result

    if walln == 3: # 벽이 세개 세워졌을때 비로소 aftergraph에 반영 후 감염 돌림.
        for i in range(n):
            for j in range(m):
                after_graph[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if after_graph[i][j] == VIRUS:
                    infect(i, j)
        result = max(result, get_blankn())
        return
    for i in range(n): # 그게 아니면 벽 세우는데 집중.
        for j in range(m):
            if graph[i][j] == BLANK: # XXX : 이 부분이 잘 이해가 가지 않는다. 
                graph[i][j] = WALL
                walln += 1
                dfs(walln)
                graph[i][j] = BLANK
                walln -= 1

dfs(0)
print(result)

