'''
# notes
mtrx 4*4
각 물고기는 번호와 방향을 가짐
번호 : 1~16 각 하나씩
방향 : 8방향

상어는 0,0 물고기 먹고 0,0에 들어감. 방향 카피.

물고기 이동:
    번호 작은것부터.
    이동가능 : 빈칸, 다른물고기 있는 칸 (swap)
    이동불가 : 경계막힘, 상어
    이동 가능할때까지 반시계 회전, 그래도 안되면 포기.
    스왑당한건 이동한걸로 안침. 정직하게 반복문 돌리면 됨.

상어 이동:
    한번에 여러 칸 이동 가능.
    역시 물고기 섭취 후 방향 카피함.
    두칸 이상 이동시 사이에 있는 물고기는 안먹음.
    BLANK로는 이동불가. 무조건 먹어야함.
    이동불가시 끝.



# io
mtrx(번호, 방향)

상어가 먹을 수 있는 물고기 번호합 최대

# strategy
상어의 이동을 재귀해야 할 것 같다. 마지막에 각 경우에 대해서 재귀하면 됨.

# pseudo code
answer = 0,0물고기번호

fish_rcs = [(-1,-1), ...]

for r in range(4):
    for c in range(4):
        fi, di = mtrx[r][c]
        fish_rcs[fi] = (r, c)

fi, di = mtrx[0][0]
mtrx[0][0] = [SHARK,방향] # 매트릭스는 좌표로 찾을 수 있도록
fish_rcs[fi] = (BLANK,BLANK) # fish_rcs는 번호로 찾는거
shr, shc, shdi = 0, 0, 방향

result = 0

def simulate(result):
    for fi in range(1, 17): # 첫 물고기부터
        r, c = fish_rcs[fi]
        if r == BLANK: # 이미 먹힌 물고기에게 조의를..
            continue

        for tmp_di in range(di, di+8):
            이동가능하다면:
                이동
                break

    shark_dist = 1

    while True:
        dr, dc =
        new_shr, new_shc = shr +
        if 잡아먹을수있어(new_shr, new_shc):
            fi, di = mtrx[new_shr][new_shc]
            잡아먹고 상어 옮기고 그 상태 넘겨서 재귀
    잡아먹을 수 없는 경우라면:
        결과값 더 크게 나올 수 있다면 갱신


    new
    shark_dist += 1


'''
from copy import deepcopy

SHARK = 0
BLANK = [-1, -1]
ds = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1),
      (1, 0), (1, 1), (0, 1), (-1, 1)]  # 1~16

mtrx = [[]] * 4
for r in range(4):
    row = list(map(int, input().split()))
    mtrx[r].append([row[0], row[1]])
    mtrx[r].append([row[2], row[3]])
    mtrx[r].append([row[4], row[5]])
    mtrx[r].append([row[6], row[7]])

answer = 0
fish_rcs = [BLANK] * 17

for r in range(4):
    for c in range(4):
        fi, di = mtrx[r][c]
        fish_rcs[fi] = (r, c)

fi, di = mtrx[0][0]
shr, shc, shdi = 0, 0, di
mtrx[0][0] = [SHARK, di]
fish_rcs[fi] = BLANK


def subsolution(result, mtrx, fish_rcs, shr, shc, shdi):
    global answer
    mtrx = deepcopy(mtrx)
    fish_rcs = deepcopy(fish_rcs)
    for fi in range(1, 17):  # 물고기의 이동
        fr, fc = fish_rcs[fi]
        _, di = mtrx[fr][fc]
        if fr == -1:
            continue
        for tmp_di in range(di, di + 8):
            dr, dc = ds[tmp_di]
            newr, newc = fr + dr, fc + dc
            if not (0 <= newr < 4 and 0 <= newc < 4):
                continue
            newi, newd = mtrx[newr][newc]
            if newi != SHARK:  # 이동가능하다면
                mtrx[fr][fc], mtrx[newr][newc] = mtrx[newr][newc], mtrx[fr][fc]
                fish_rcs[fi], fish_rcs[newi] = fish_rcs[newi], fish_rcs[fi]
                break

    power = 1
    shdr, shdc = ds[shdi]
    continuing = False
    while True:
        new_shr, new_shc = shr + shdr * power, shc + shdc * power
        if not (0 <= new_shr < 4 and 0 <= new_shc):
            break

        # 뭐시기
        if mtrx[new_shr][new_shc] != BLANK:
            continuing = True
            fi, di = mtrx[new_shr][new_shc]
            fish_rcs_arg = deepcopy(fish_rcs)
            mtrx_arg = deepcopy(mtrx)
            fish_rcs_arg[fi] = BLANK
            fish_rcs_arg[SHARK] = (new_shr, new_shc)
            mtrx_arg[shr][shc] = BLANK
            mtrx_arg[new_shr][new_shc] = (SHARK, di)
            subsolution(result + fi, mtrx_arg, fish_rcs_arg, new_shr, new_shc, di)

        power += 1

    if not continuing:
        answer = max(answer, result)


subsolution(fi, mtrx, fish_rcs, 0, 0, shdi)
print(answer)
