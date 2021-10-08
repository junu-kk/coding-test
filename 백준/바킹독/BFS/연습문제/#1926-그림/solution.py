'''
<io>
6 5 # r, c
1 1 0 1 1 # 1은 칠해진 부분
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

4 # 그림의 개수
9 # 가장 넓은 그림

<notes>
그림이 없는경우는 넓은그림의 넓이 0

<strategy>
visit_t 따로 만들고
각 점들마다 BFS 조지면 될것같다.
넓이는.. 하나 visit할때마다 1씩 올려주면 되겠다.

visit_t = [[False]*cn for _ in range(rn)]
picture_max_size = 0


def bfs(r, c):
    global picture_max_size
    q = deque([(r, c)])
    visit_t[r][c] = True
    picture_size = 1
    while q:
        r, c = q.popleft()
        for dr, dc in ds:
            if 범위안(r+dr, c+dc) and not visit_t[r][c]:
                q.append((newr, newc))
                visit_t[newr][newc] = True
                picture_size += 1

    picture_max_size = max(pms, picture_size)



for r in range(rn):
    for c in range(cn):
        if jido[r][c] == COLORED and not visit_t[r][c]:
            bfs(r, c)
            picture_n += 1


'''

from collections import deque

COLORED = 1
BLANK = 0

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

rn, cn = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(rn)]
visit_t = [[False] * cn for _ in range(rn)]
picture_max_size = 0
picture_n = 0


def bfs(r: int, c: int):
    global picture_max_size
    q = deque([(r, c)])
    visit_t[r][c] = True
    picture_size = 1
    while q:
        r, c = q.popleft()
        for dr, dc in ds:
            newr, newc = r + dr, c + dc
            if 0 <= newr < rn and 0 <= newc < cn and jido[newr][newc] == COLORED and not visit_t[newr][newc]:
                q.append((newr, newc))
                visit_t[newr][newc] = True
                # print(f'{newr}, {newc} 색칠')
                picture_size += 1

    picture_max_size = max(picture_max_size, picture_size)


for r in range(rn):
    for c in range(cn):
        if jido[r][c] == COLORED and not visit_t[r][c]:
            # print(f'{r}, {c}에서부터 bfs 시작')
            bfs(r, c)
            picture_n += 1

print(picture_n)
print(picture_max_size)
