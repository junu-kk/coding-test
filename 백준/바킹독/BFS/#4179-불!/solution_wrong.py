'''
아 좀 애매하네.
dfs bfs 문제인것같긴한데

일단 bfs로 접근하고, 각 depth가 깊어질때마다
0. 사이즈 하나씩 늘려주고
1. fire 퍼지게하고
2. 상하좌우로 r, c 옮겨주고
3. 만약 끄트머리에 도달한다면 depth 출력해주고
4. 큐가 비어버린다면 impossible 출력해주자.


'''
import pprint
from collections import deque
from copy import deepcopy

WALL = '#'
BLANK = '.'
FIRE = 'F'
TDR = 'T'
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def spread_fire(jido: list, rn: int, cn: int):
    new_jido = deepcopy(jido)
    for r in range(rn):
        for c in range(cn):
            if jido[r][c] == FIRE:
                for dr, dc in ds:
                    newr, newc = r + dr, c + dc
                    if 0 <= newr < rn and 0 <= newc < cn and jido[newr][newc] == BLANK:
                        new_jido[newr][newc] = FIRE

    return new_jido


def get_init_pos(rn, cn, jido):
    for r in range(rn):
        for c in range(cn):
            if jido[r][c] == 'J':
                return r, c

    return 0


def solution():
    rn, cn = map(int, input().split())
    jido = [[TDR] * (cn + 2)]
    for _ in range(rn):
        jido.append([TDR] + list(input()) + [TDR])
    jido.append([TDR] * (cn + 2))

    rn += 2
    cn += 2

    # pprint.pprint(jido)
    r, c = get_init_pos(rn, cn, jido)
    jido[r][c] = BLANK

    q = deque([[r, c, 0]])
    while q:
        r, c, depth = q.popleft()
        jido = spread_fire(jido, rn, cn)
        pprint.pprint(jido)
        print()
        for dr, dc in ds:
            newr, newc = r + dr, c + dc
            if 0 <= newr < rn and 0 <= newc < cn and jido[newr][newc] == BLANK:
                if jido[newr][newc] == TDR:
                    return depth+1
                q.append([newr, newc, depth + 1])



    return 'IMPOSSIBLE'


print(solution())
