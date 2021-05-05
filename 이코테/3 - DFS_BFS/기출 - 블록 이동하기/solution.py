# 답 참조하며 짬.

from collections import deque

WALL = 1
BLANK = 0
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_next_locs(loc, mtrx):
    next_locs = []
    loc = list(loc)
    r1, c1, r2, c2 = loc[0][0], loc[0][1], loc[1][0], loc[1][1]
    for d in ds:
        dr, dc = d
        r1_next, c1_next, r2_next, c2_next = r1+dr, c1+dc, r2+dr, c2+dc
        if mtrx[r1_next][c1_next] == BLANK and mtrx[r2_next][c2_next] == BLANK:
            next_locs.append({(r1_next, c1_next), (r2_next, c2_next)})
    if r1 == r2:  # 가로일때
        if mtrx[r1-1][c1] == BLANK and mtrx[r2-1][c2] == BLANK:
            next_locs.append({(r1, c1), (r1-1, c1)})  # 세로하나
            next_locs.append({(r2, c2), (r2-1, c2)})  # 세로둘
        if mtrx[r1+1][c1] == BLANK and mtrx[r2+1][c2] == BLANK:
            next_locs.append({(r1, c1), (r1+1, c1)})  # 세로하나
            next_locs.append({(r2, c2), (r2+1, c2)})  # 세로둘
    elif c1 == c2:  # 세로일때
        if mtrx[r1][c1-1] == BLANK and mtrx[r2][c2-1] == BLANK:
            next_locs.append({(r1, c1), (r1, c1-1)})  # 세로하나
            next_locs.append({(r2, c2), (r2, c2-1)})  # 세로둘
        if mtrx[r1+1][c1] == BLANK and mtrx[r2+1][c2] == BLANK:
            next_locs.append({(r1, c1), (r1, c1+1)})  # 가로하나
            next_locs.append({(r2, c2), (r2, c2+1)})  # 가로둘

    return next_locs


def solution(board):
    n = len(board)
    new_board = [[WALL]*(n+2) for _ in range(n+2)]
    for r in range(n):
        for c in range(n):
            new_board[r+1][c+1] = board[r][c]

    q = deque()
    visit_t = []
    loc = {(1, 1), (1, 2)}

    q.append((loc, 0))
    visit_t.append(loc)

    while q:
        loc, cost = q.popleft()
        if (n, n) in loc:
            return cost

        for next_loc in get_next_locs(loc, new_board):
            if next_loc not in visit_t:
                q.append((next_loc, cost+1))
                visit_t.append(next_loc)
    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
