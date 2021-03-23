rn, cn = map(int, input().split())
jido = [list(map(int, input())) for _ in range(rn)]

BLANK = 0
WALL = 1
TRAVERSED = 2

answer = 0

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_in_jido(r, c):
    if 0 <= r < rn and 0 <= c < cn:
        return True
    return False


def spread(r, c):
    for d in ds:
        dr, dc = d
        if is_in_jido(r+dr, c+dc) and jido[r+dr][c+dc] == BLANK:
            jido[r+dr][c+dc] = TRAVERSED
            spread(r+dr, c+dc)


for r in range(rn):
    for c in range(cn):
        if jido[r][c] == BLANK:
            answer += 1
            spread(r, c)


print(answer)
