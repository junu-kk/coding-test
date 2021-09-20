'''
<input&output>
places
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]



return
[1,0,1,1,1]
모두 지키고 있으면 1, 하나라도 안지키고 있으면 0

<notes>
거리 : 가로거리 + 세로거리가 2를 넘어선 안됨. (벽 제외)
places는 5바이5 다섯개로 고정.

P : 응시자
O : 빈테이블
X : 벽


<strategy>
아 솔직히 그냥 빡구현 각인데. BFS로도 풀릴 것 같고.
-> 둘 다 해보자 ㅇㅇ.

각 5*5의 place마다 쭉 돌면서, p가 있다면 다음을 반복한다.

<빡구현>
r-2~r+2 c-2~c+2 전수검사 하면서 (범위 안에서)
    맨해튼거리 1인데 플레이어가 있다 : return 0
    맨해튼거리가 2인데 플레이어가 있다 : 다음의 경우 빠꾸.
        r값이 같으면서 c값의 평균이 BLANK다
        c값이 같으면서 r값의 평균이 BLANK다
        기타의 경우: r값 c값 서로 하나씩 swap해준 두 좌표 중 하나라도 BLANK다 : 빠꾸

<BFS>
한번 검사한 구역은 청정구역이라고 해도 괜찮다. 즉 visit_t를 따로 선언해도 좋을 것.
    상하좌우 검사 -> 있으면 return 0
    상하좌우의 상하좌우 검사 -> 플레이어가 있으면
'''
PLAYER = 'P'
BLANK = 'O'
WALL = 'X'

DANGER = 0
SAFE = 1


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_grdg_status(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == PLAYER:
                for tmp_r in range(r - 2, r + 3):
                    for tmp_c in range(c - 2, c + 3):
                        # 범위에 없으면 빠꾸
                        if not (0 <= tmp_r < 5 and 0 <= tmp_c < 5):
                            continue

                        distance = get_distance((r, c), (tmp_r, tmp_c))

                        '''
                        맨해튼거리 1인데 플레이어가 있다 : return DANGER
                        맨해튼거리가 2인데 플레이어가 있다 : 다음의 경우 빠꾸.
                            r값이 같으면서 c값의 평균이 BLANK다
                            c값이 같으면서 r값의 평균이 BLANK다
                            기타의 경우: r값 c값 서로 하나씩 swap해준 두 좌표 중 하나라도 BLANK다 : 빠꾸
                        이 모든 걸 다 통과하면 return SAFE
                        '''

                        # 거리 1인경우
                        if distance == 1 and place[tmp_r][tmp_c] == PLAYER:
                            return DANGER

                        # 거리 2인경우 -> 아 일직선에 있는 경우도 있었구나. 실수 ^^.
                        elif distance == 2 and place[tmp_r][tmp_c] == PLAYER:
                            if r == tmp_r:
                                if place[r][(c + tmp_c) // 2] == BLANK:
                                    return DANGER
                                else:
                                    continue
                            elif c == tmp_c:
                                if place[(r + tmp_r) // 2][c] == BLANK:
                                    return DANGER
                                else:
                                    continue
                            elif not (place[r][tmp_c] == WALL and place[tmp_r][c] == WALL):
                                return DANGER
    return SAFE


def solution(places):
    answer = []
    for place in places:
        grdg_status = get_grdg_status(place)
        answer.append(grdg_status)

    return answer