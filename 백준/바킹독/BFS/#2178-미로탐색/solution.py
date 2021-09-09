'''
<io>
input
4 6 # rn cn
101111 # jido
101010
101011
111011

return
15

<notes>
1 : BLANK
0 : WALL

지나야 하는 최소 칸 수
시작위치와 도착위치도 포함. 불가능한 경우 없음.

<strategy>
거리를 측정해야 하므로, visit_t 대신 depth_t로 갑니다.
그렇게 하다가 rn-1, cn-1에 도달하면 바로 리턴해주면 됨.

'''
from collections import deque


def solution():
    BLANK = 1
    WALL = 0
    UNVISITED = -1

    ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    rn, cn = map(int, input().split())
    jido = [list(map(int, list(input()))) for _ in range(rn)]
    depth_t = [[UNVISITED] * cn for _ in range(rn)]

    q = deque([(0, 0)])
    depth_t[0][0] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in ds:
            newr, newc = r + dr, c + dc
            if 0 <= newr < rn and 0 <= newc < cn and jido[newr][newc] == BLANK and depth_t[newr][newc] == UNVISITED:
                q.append((newr, newc))
                depth_t[newr][newc] = depth_t[r][c] + 1

                # 종료가 될 때
                if newr == rn - 1 and newc == cn - 1:
                    return depth_t[newr][newc]
    return -1

print(solution())
