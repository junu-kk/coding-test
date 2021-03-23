from collections import deque
from sys import stdin
input = stdin.readline

BLANK = 1
WALL = 0

rn, cn = map(int, input().split())
jido = [list(map(int, input().rstrip())) for _ in range(rn)]

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_in_map(r, c):
    global rn, cn
    if 0 <= r < rn and 0 <= c < cn:
        return True
    return False


def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for d in ds:
            newr, newc = r+d[0], c+d[1]
            if is_in_map(newr, newc) and jido[newr][newc] == BLANK:
                # 이 부분이 핵심인 것 같다. 다른 테이블이 아닌 지도 자체에 기록을 하는 것.
                # 처음 방문하는 경우에만 기록해야 한다.
                jido[newr][newc] = jido[r][c] + 1
                q.append((newr, newc))

    # 그렇게 쭉 돌게 된다면 결국 모든 blank들을 탐색하게 될 것
    return jido[rn-1][cn-1]


print(bfs(0, 0))
# print(jido)
