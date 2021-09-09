'''
<io>
4 4 rn cn
#### jido
#JF#
#..#
#..#

<notes>
지훈이가 불타기전 탈출할 수 있는가?
얼마나 빨리 탈출할 수 있는가?
가장자리에서 하나 더 밖으로 나가면 탈출 가능 (jido를 넓힐까?)

WALL = #
JIHUN = J
FIRE = F
BLANK = .

탈출 못하면 IMPOSSIBLE
가능하면 가장빠른 탈출시각

<strategy>
최단depth이므로 bfs 써야함.
rn cn 받았지만 +2씩 해주고, jido 넓혀주고, 지훈이 움직일때마다 테두리인지 확인해주자.
불이 먼저 움직이고 지훈이가 움직인다 -> 큐 두개.

다만 지훈이는 한명인데 불은 여러군데 있을 수 있음 -> 0으로 일단은 시작해서 하나씩 퍼져나가야겠다.
지훈이가 발을 밟는 시점에 불이 있는지 또한 판단해야 할 것.
즉 지도에 "언제 불이 번졌는지" 저장해야 함.

지훈이의 첫 r, c만 저장하고 BLANK로 바꿔주자.

jq = deque((지훈r, 지훈c, mvcnt0))
fq = deque([불위치1, 불위치2, ...])

while fq:
    r, c = fq.popleft()
    for dr, dc in ds:
        newr, newc = r+dr, c+dc
        if 0<=newr<rn and 0<=newc<cn:
            continue
        if jido[newr][newc] == BLANK:
            jido[newr][newc] = jido[r][c] + 1
            fq.append((newr, newc))

while jq:
    r, c, mv_cnt = jq.popleft()
    for dr, dc in ds:
        newr, newc, new_mv_cnt = r+dr, c+dc, mv_cnt+1
        if 0<= newr < rn and 0<= newc < cn:
            continue
        지훈이의 new_mv_cnt가 더 작아야함. 불과 같아서도 안됨.
        if jido[newr][newc] == WALL or new_mv_cnt < jido[newr][newc]:
            continue
        q.append((newr, newc, new_mv_cnt))
        if hooray(newr, newc):
            return new_mv_cnt

'''
import pprint
from collections import deque


def solution():
    WALL = '#'
    JIHUN = 'J'
    FIRE = 'F'
    BLANK = '.'

    rn, cn = map(int, input().split())
    jido = [[BLANK] * cn for _ in range(rn)]

    temp_jido = [list(input()) for _ in range(rn)]

    jq = deque()
    fq = deque()

    visit_t = [[False] * cn for _ in range(rn)]

    for r in range(rn):
        for c in range(cn):
            if temp_jido[r][c] == JIHUN:
                jido[r][c] = BLANK
                visit_t[r][c] = True
                jq.append((r, c, 0))
            elif temp_jido[r][c] == FIRE:
                jido[r][c] = 0
                fq.append((r, c))
            else:
                jido[r][c] = temp_jido[r][c]

    '''
    while fq:
        r, c = fq.popleft()
        for dr, dc in ds:
            newr, newc = r+dr, c+dc
            if 0<=newr<rn and 0<=newc<cn:
                continue
            if jido[newr][newc] == BLANK:
                jido[newr][newc] = jido[r][c] + 1
                fq.append((newr, newc))
    
    while jq:
        r, c, mv_cnt = jq.popleft()
        for dr, dc in ds:
            newr, newc, new_mv_cnt = r+dr, c+dc, mv_cnt+1
            if 0<= newr < rn and 0<= newc < cn:
                continue
            지훈이의 new_mv_cnt가 더 작아야함. 불과 같아서도 안됨.
            if jido[newr][newc] == WALL or new_mv_cnt < jido[newr][newc]:
                continue
            q.append((newr, newc, new_mv_cnt))
            if hooray(newr, newc):
                return new_mv_cnt
    '''

    def hooray(newr, newc):
        if newr in (0, rn - 1) or newc in (0, cn - 1):
            return True
        return False

    ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # print(fq)
    while fq:
        r, c = fq.popleft()
        for dr, dc in ds:
            newr, newc = r + dr, c + dc
            if not (0 <= newr < rn and 0 <= newc < cn):
                continue
            if jido[newr][newc] == BLANK:
                jido[newr][newc] = jido[r][c] + 1
                fq.append((newr, newc))

    pprint.pprint(jido)

    while jq:
        # print(jq)
        r, c, mv_cnt = jq.popleft()
        print(r, c, mv_cnt)
        for dr, dc in ds:
            newr, newc, new_mv_cnt = r + dr, c + dc, mv_cnt + 1

            if not (0 <= newr < rn and 0 <= newc < cn):
                continue


            if visit_t[newr][newc]:
                continue

            if jido[newr][newc] != BLANK and jido[newr][newc] <= new_mv_cnt:
                continue

            if hooray(newr, newc):
                return new_mv_cnt+1

            jq.append((newr, newc, new_mv_cnt))
            visit_t[newr][newc] = True

    return 'IMPOSSIBLE'


print(solution())
