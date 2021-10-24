from copy import deepcopy

mtrx = [[None] * 4 for _ in range(4)]
for r in range(4):
    row = list(map(int, input().split()))
    for c in range(4):
        # print(r, c)
        mtrx[r][c] = [row[c * 2], row[c * 2 + 1] - 1]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def turn_left(d):
    return (d + 1) % 8


answer = 0


def find_fish(mtrx, fi):
    for r in range(4):
        for c in range(4):
            if mtrx[r][c][0] == fi:
                return r, c
    return None


def move_fishes(mtrx, shr, shc):
    for fi in range(1, 17):
        pos = find_fish(mtrx, fi)
        if pos is not None:
            r, c = pos
            d = mtrx[r][c][1]
            for _ in range(8):
                newr = r + dr[d]
                newc = c + dc[d]
                if 0 <= newr < 4 and 0 <= newc < 4:
                    if not (newr == r and newc == r):
                        mtrx[r][c][1] = d
                        mtrx[r][c], mtrx[newr][newc] = mtrx[newr][newc], mtrx[r][c]
                        break
                d = turn_left(d)


def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 쭉 이동하기
    for i in range(4):
        now_x += dr[direction]
        now_y += dc[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(mtrx, now_x, now_y, total):
    global answer
    mtrx = deepcopy(mtrx)  # 리스트를 통째로 복사

    total += mtrx[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    mtrx[now_x][now_y][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_fishes(mtrx, now_x, now_y)  # 전체 물고기 이동 시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(mtrx, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        answer = max(answer, total)  # 최댓값 저장
        return
        # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(mtrx, next_x, next_y, total)


# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(mtrx, 0, 0, 0)
print(answer)
