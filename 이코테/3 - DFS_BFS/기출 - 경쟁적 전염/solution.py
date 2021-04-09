from copy import deepcopy
from sys import stdin
input = stdin.readline

n, virus_n = map(int, input().rstrip().split())
jido = [list(map(int, input().rstrip().split())) for _ in range(n)]
target_time, target_r, target_c = map(int, input().rstrip().split())
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_in_map(r, c):
    global n
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def spread(mtrx: list):
    global n
    INF = int(1e9)
    spread_record = deepcopy(mtrx)  # 퍼진 경우엔 마이너스 붙여서 반영하자.
    # print(f'스프레드레코드 이전 : {spread_record}')
    for r in range(n):
        for c in range(n):
            if mtrx[r][c] > 0 and spread_record[r][c] > 0:
                for d in ds:
                    dr, dc = d
                    # 원래 무언가가 있었다면 넘어가야 함. 즉 <=0일때만 가능.
                    if is_in_map(r+dr, c+dc) and (mtrx[r][c] < -spread_record[r+dr][c+dc] or spread_record[r+dr][c+dc] == 0):
                        mtrx[r+dr][c+dc] = mtrx[r][c]
                        spread_record[r+dr][c+dc] = -mtrx[r][c]

    # print(f'스프레드레코드 이후 : {spread_record}')
    return mtrx


for _ in range(target_time):
    jido = spread(jido)
    # print('반영후 : ', jido)

print(jido[target_r-1][target_c-1])
