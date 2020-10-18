'''
문제는 이해를 했는데
답을 이해하지 못하겠음
나중에 다시 한번 꼭 풀어보자.
'''

from collections import deque

n, L, R = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = 0

def process(r, c, index):
    united = []
    united.append((r, c))
    q = deque()
    q.append((r, c))
    union[r][c] = index
    summary = graph[r][c]
    count = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            newr = r + dr[i]
            newc = c + dc[i]
            if 0 <= newr < n and 0 <= newc < n and union[newr][newc] == -1:
                if L <= abs(graph[newr][newc] - graph[r][c]) <= R:
                    q.append((newr, newc))
                    union[newr][newc] = index
                    summary += graph[newr][newc]
                    count += 1
                    united.append((newr, newc))
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1
print(total_count)
    