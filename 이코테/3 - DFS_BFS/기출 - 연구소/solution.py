from itertools import combinations
from copy import deepcopy
from sys import stdin
input = stdin.readline

BLANK = 0
WALL = 1
VIRUS = 2

rn, cn = map(int, input().rstrip().split())
jido = [list(map(int, input().rstrip().split())) for _ in range(rn)]

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0


def is_in_map(r, c):
    global rn, cn
    if 0 <= r < rn and 0 <= c < cn:
        return True
    return False


blank_locs = []
for r in range(rn):
    for c in range(cn):
        if jido[r][c] == BLANK:
            blank_locs.append((r, c))


def spread_virus(r, c, mtrx):
    for d in ds:
        dr, dc = d
        if is_in_map(r+dr, c+dc) and mtrx[r+dr][c+dc] == BLANK:
            mtrx[r+dr][c+dc] = VIRUS
            spread_virus(r+dr, c+dc, mtrx)


def count_blank_n(mtrx):
    blank_n = 0
    for row in mtrx:
        blank_n += row.count(BLANK)
    return blank_n


for comb in combinations(blank_locs, 3):
    jido_temp = deepcopy(jido)
    for each in comb:
        r, c = each
        jido_temp[r][c] = WALL
    for r in range(rn):
        for c in range(cn):
            if jido_temp[r][c] == VIRUS:
                spread_virus(r, c, jido_temp)

    answer = max(answer, count_blank_n(jido_temp))

print(answer)
