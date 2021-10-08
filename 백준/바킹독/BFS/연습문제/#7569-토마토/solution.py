'''
<io>
5 3 1 cn rn hn
0 -1 0 0 0 # bupee
-1 -1 0 1 1
0 0 0 1 1

-1
<notes>
3차원의 d를 선언해야할듯.
쫙쫙 익는 토마토가 다 익으려면 몇 일이 걸릴까?
물론 토마토가 안들어있는 칸도 있음.

1 : 익은 토마토
0 : 익지 않은 토마토
-1 : WALL


원래부터 다익어있었으면 0
아무리 해도 다 못익으면 -1

<strategy>
여러 시작점일때의 BFS니까.. 큐에 그냥 다 때려넣고 시작하면 되겠다.
다만 그 경우엔 익는 그 경계를 어떻게 찾지?
방금 생각한 똥같은 방법 : 큐에 구분자를 하나 넣어준다. 뭐.. -1 -1 -1 이런 식으로.
이거 만나면 time_elapsed += 1 해주면 될 것 같긴 함.
=> 그러면 안되는 이유가
일단 해보자 ㅋ

3차원 BFS 함 해봅시다.
입력받을때 토마토 개수 다 세주고,
토마토 익힐때마다 도달했는지 확인해주고

아 근데 하다보니
그냥 bupee를 0 1 2 3 ... 이러한 time으로 채워도 될 것 같네.

'''
import pprint
from collections import deque


def solution():
    IKTO = 1
    NOT_IKTO = 0
    WALL = -1

    ds = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    cn, rn, hn = map(int, input().split())
    bupee = []
    left_tomato_n = 0
    q = deque()
    for h in range(hn):
        jido = []
        for r in range(rn):
            col = list(map(int, input().split()))
            left_tomato_n += col.count(NOT_IKTO)
            jido.append(col)
            for c in range(cn):
                if col[c] == IKTO:
                    q.append((h, r, c))
        bupee.append(jido)

    if left_tomato_n == 0:
        return 0
    # pprint.pprint(bupee)
    while q:
        h, r, c = q.popleft()

        for dh, dr, dc in ds:
            newh, newr, newc = h + dh, r+dr, c+dc
            if not (0 <= newr < rn and 0 <= newc < cn and 0 <= newh < hn):
                continue

            if bupee[newh][newr][newc] == NOT_IKTO:
                bupee[newh][newr][newc] = bupee[h][r][c] + 1
                q.append((newh, newr, newc))
                left_tomato_n -= 1
                if left_tomato_n == 0:
                    return bupee[h][r][c]
    return -1

print(solution())