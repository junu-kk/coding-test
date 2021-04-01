

BLANK = 0

n, k = map(int, input().split())
shg = []
viruses = [] # 종류, 시간, r, c
for i in range(n):
    shg.append(list(map(int, input().split())))
    for j in range(n):
        if shg[i][j] != BLANK:
            viruses.append((shg[i][j], 0, i, j))

target_t, target_r, target_c = map(int, input().split())
from collections import deque

q = deque(sorted(viruses)) # 낮은게 앞으로 옴.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while q:
    virus, t, r, c = q.popleft()
    if t == target_t: # 때가 되면 끝
        break
    for i in range(4):
        newr = r + dr[i]
        newc = c + dc[i]
        if 0 <= newr < n and 0 <= newc < n: # 범위 안에 있는 경우
            if shg[newr][newc] == BLANK:
                shg[newr][newc] = virus
                q.append((virus, t+1, newr, newc))


print(shg[target_r-1][target_c-1])