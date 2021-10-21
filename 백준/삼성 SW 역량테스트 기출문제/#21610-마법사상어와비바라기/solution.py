'''
# notes
범위 벗어나면 그 반대쪽에 영향.
11 ~ nn
비바라기 시전 시 왼쪽아래 2*2만큼 비구름 생김.

방향 : 1~8, 왼쪽부터 시계방향

이동 명령 시
1. 모든 구름이 바람따라 이동
2. 구름자리에 물+=1
3. 구름 없어짐
4. 물이 증가한 칸 대각선에 += 1(경계 넘지 않음.)
5. 물의 양이 2 이상이면 구름생성, 물-=2 but 3번의 구름엔 해당하지 않아야 함.

result : 물양합

# io
5 4 # 사이즈, cmd수
0 0 1 0 2 #
2 3 2 1 0
4 3 2 9 0
1 0 2 9 0
8 8 2 1 0
1 3 # 방향, 거리
3 4
8 1
4 8

# strategy
구름을 grm_t로 관리 or 구름 rc를 저장.

1. 모든 구름이 바람따라 이동
2. 구름자리에 물+=1
3. 구름 없어짐
4. 물이 증가한 칸 대각선에 += 1(경계 넘지 않음.)
5. 물의 양이 2 이상이면 구름생성, 물-=2 but 3번의 구름엔 해당하지 않아야 함.

# pseudo code
winds로 하는 편이 낫겠다.




'''
from pprint import pprint

ds = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dks = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
n, cmd_n = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(n)]
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]


def adjust_loc(x):
    if 0 <= x < n:
        return x
    elif x >= n:
        while not (0 <= x < n):
            x -= n
    else:
        while not (0 <= x < n):
            x += n

    return x


for _ in range(cmd_n):
    di, dist = map(int, input().split())
    dr, dc = ds[di]
    '''
    2. 구름자리에 물+=1
    3. 구름 없어짐
    4. 물이 증가한 칸 대각선에 += 1(경계 넘지 않음.)
    5. 물의 양이 2 이상이면 구름생성, 물-=2 but 3번의 구름엔 해당하지 않아야 함.
    '''
    for i in range(len(clouds)):
        cr, cc = clouds[i]
        cr = adjust_loc(cr + dr * dist)
        cc = adjust_loc(cc + dc * dist)
        clouds[i] = [cr, cc]

    more_ups = []
    for cr, cc in clouds:
        mtrx[cr][cc] += 1
    for cr, cc in clouds:
        more_up = 0
        for dkr, dkc in dks:
            newr, newc = cr + dkr, cc + dkc
            if 0 <= newr < n and 0 <= newc < n and mtrx[newr][newc] > 0:
                more_up += 1

        more_ups.append((cr, cc, more_up))
    for r, c, more_up in more_ups:
        mtrx[r][c] += more_up

    tmp_winds = [[False] * n for _ in range(n)]
    for cr, cc in clouds:
        tmp_winds[cr][cc] = True
    clouds.clear()

    for r in range(n):
        for c in range(n):
            if mtrx[r][c] >= 2 and not tmp_winds[r][c]:
                mtrx[r][c] -= 2
                clouds.append((r, c))

    # pprint(mtrx)
    # print(clouds)
answer = 0
for row in mtrx:
    answer += sum(row)
print(answer)
