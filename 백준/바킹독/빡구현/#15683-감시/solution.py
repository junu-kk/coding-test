'''
<io>
4 6 # rn cn jido
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0

20 # 사각지대 최소크기

<notes>
방향은 알아서 설정
cctv끼리 통과 가능

<strategy>
cctv를 모두 찾고, n개가 있으면 n중포문을 돌려서
모든 경우의 수에 대해 감시값을 갱신하는 식으로 가면 됨.

관건은
- n중포문을 어떻게 구현하는가
    백트래킹처럼 재귀를 써야 하는가?
    ==> 아마 그래야 할 것 같다.
    전체 카메라 개수 파악한 다음에
    카메라 만날때마다 depth+1로 재귀 돌리고,
    depth가 차면 그 때 answer 갱신해주는 방식으로.
- jido 복사 어떻게 할 것인가
    재귀 돌릴때마다 복사해줘야지 뭐.
    다만 감시가능 테이블은 jido와 분리해서 생각하는게 좋을것같다.
'''
from copy import deepcopy

BLANK = 0
WALL = 6

u, r, d, l = (-1, 0), (0, 1), (1, 0), (0, -1)
ds1 = [[u], [r], [d], [l]]  # 4가지
ds2 = [[r, l], [u, d]]  # 2가지
ds3 = [[u, r], [r, d], [d, l], [l, u]]  # 4가지
ds4 = [[l, u, r], [u, r, d], [r, d, l], [d, l, u]]  # 4가지
ds5 = [[u, r, d, l]]  # 1가지
ds = [[], ds1, ds2, ds3, ds4, ds5]

rn, cn = map(int, input().split())
answer = rn * cn
cam_locs = []
jido = []
for r in range(rn):
    row = list(map(int, input().split()))
    for c in range(cn):
        if 1 <= row[c] <= 5:
            cam_locs.append((r, c, row[c]))
    jido.append(row)

cam_n = len(cam_locs)

'''
관건은
- n중포문을 어떻게 구현하는가
    백트래킹처럼 재귀를 써야 하는가?
    ==> 아마 그래야 할 것 같다.
    전체 카메라 개수 파악한 다음에
    카메라 만날때마다 depth+1로 재귀 돌리고,
    depth가 차면 그 때 answer 갱신해주는 방식으로.
- jido 복사 어떻게 할 것인가
    재귀 돌릴때마다 복사해줘야지 뭐.
    다만 감시가능 테이블은 jido와 분리해서 생각하는게 좋을것같다.
'''


def subsol(depth, sagak_mtrx):
    global cam_n, answer

    if depth == cam_n:
        sagak_n = 0
        for row in sagak_mtrx:
            for sagak in row:
                if sagak:
                    sagak_n += 1
        answer = min(answer, sagak_n)
        return

    cam_r, cam_c, cam_type = cam_locs[depth]
    cam_ds = ds[cam_type]
    for cam_d in cam_ds:  # 후보
        cam_d_mtrx = deepcopy(sagak_mtrx)
        for dr, dc in cam_d:  # 상세 d
            i = 1
            while True:
                idr, idc = i * dr, i * dc
                newr, newc = cam_r + idr, cam_c + idc
                if not (0 <= newr < rn and 0 <= newc < cn) or jido[newr][newc] == WALL:
                    break
                cam_d_mtrx[newr][newc] = False
                i += 1

        subsol(depth + 1, cam_d_mtrx)  # 그 매트릭스로 재귀


# 사각지대는 첨에 싹 다 True로 초기화해야함.
# 벽이랑 카메라랑만 False로 해주고.

init_mtrx = [[True] * cn for _ in range(rn)]
for r in range(rn):
    for c in range(cn):
        if jido[r][c] >= 1:
            init_mtrx[r][c] = False

subsol(0, init_mtrx)
print(answer)