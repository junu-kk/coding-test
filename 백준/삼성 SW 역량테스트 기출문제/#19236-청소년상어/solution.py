# ndb 풀이 참조, 아니 근데 이게 왜틀렸는지 모르겠네
from copy import deepcopy

mtrx = [[None] * 4 for _ in range(4)]
for r in range(4):
    row = list(map(int, input().split()))
    for c in range(4):
        mtrx[r][c] = [row[c * 2], row[c * 2 + 1] - 1]
# print(mtrx)
drs = [-1, -1, 0, 1, 1, 1, 0, -1] * 2
dcs = [0, -1, -1, -1, 0, 1, 1, 1] * 2
ds = list(zip(drs, dcs))
# print(ds)
answer = 0
BLANK = -1


def get_fr_fc(mtrx, fi):
    for r in range(4):
        for c in range(4):
            if mtrx[r][c][0] == fi:
                return r, c
    return BLANK, BLANK


def get_av_shr_shcs(mtrx, shr, shc):
    av_shr_shcs = []
    di = mtrx[shr][shc][1]
    dr, dc = ds[di]
    for _ in range(4):
        shr += dr
        shc += dc
        if 0 <= shr < 4 and 0 <= shc < 4:
            if mtrx[shr][shc][0] != BLANK:
                av_shr_shcs.append((shr, shc))
    print(av_shr_shcs)
    return av_shr_shcs


def subsol(mtrx, shr, shc, mid_answer):
    global answer
    mtrx = deepcopy(mtrx)

    mid_answer += mtrx[shr][shc][0]
    mtrx[shr][shc][0] = BLANK

    # 물고기의 이동
    for fi in range(1, 17):
        fr, fc = get_fr_fc(mtrx, fi)
        if (fr, fc) != (BLANK, BLANK):
            continue
        di = mtrx[fr][fc][1]
        # 아 여기서 에러가 터졌구나. 변수명 잘 구분되게 쓰자. i같은 변수명 피할것.
        for _ in range(8):
            dr, dc = ds[di]
            newr, newc = fr + dr, fc + dc
            if 0 <= newr < 4 and 0 <= newc < 4:
                if not (newr == shr and newc == shc):
                    mtrx[r][c][1] = di
                    mtrx[r][c], mtrx[newr][newc] = mtrx[newr][newc], mtrx[r][c]
                    break
            di = (di+1)%8

    # 상어의 이동
    sh_locs = get_av_shr_shcs(mtrx, shr, shc)
    if len(sh_locs) == 0:
        answer = max(answer, mid_answer)
        return

    for new_shr, new_shc in sh_locs:
        subsol(mtrx, new_shr, new_shc, mid_answer)


subsol(mtrx, 0, 0, 0)
print(answer)
