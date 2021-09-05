from collections import deque

FIRE = 'F'
PLAYER = 'J'
WALL = '#'

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    # 불이 먼저 퍼지고
    while fire_q:
        r, c = fire_q.popleft()

        for dr, dc in ds:
            newr, newc = r + dr, c + dc

            if 0 <= newr < rn and 0 <= newc < cn:
                # 아직 불이 거쳐가지 않았고, 벽으로 막혀있지 않다면 퍼지기
                if fire_depth_t[newr][newc] == 0 and jido[newr][newc] != WALL:
                    fire_depth_t[newr][newc] = fire_depth_t[r][c] + 1
                    fire_q.append((newr, newc))

    # 플레이어가 이동함
    while player_q:
        r, c = player_q.popleft()

        for dr, dc in ds:
            newr, newc = r + dr, c + dc

            if 0 <= newr < rn and 0 <= newc < cn:
                # 아직 플레이어가 거쳐가지 않았고, 벽으로 막혀지있지 않은데
                if player_depth_t[newr][newc] == 0 and jido[newr][newc] != WALL:
                    # 불길이 거치지 않았거나, 플레이어가 선수친 경우 스프레드
                    if fire_depth_t[newr][newc] == 0 or fire_depth_t[newr][newc] > player_depth_t[r][c] + 1:
                        player_depth_t[newr][newc] = player_depth_t[r][c] + 1
                        player_q.append((newr, newc))
            else:  # 범위탈출 == 플레이어의 탈출
                return player_depth_t[r][c] + 1

    return 'IMPOSSIBLE'


rn, cn = map(int, input().split())
jido = [list(input()) for _ in range(rn)]
fire_q, player_q = deque(), deque()
fire_depth_t, player_depth_t = [[0] * cn for _ in range(rn)], [[0] * cn for _ in range(rn)]

for r in range(rn):
    for c in range(cn):
        if jido[r][c] == FIRE:
            fire_q.append((r, c))
        elif jido[r][c] == PLAYER:
            player_q.append((r, c))

print(bfs())
