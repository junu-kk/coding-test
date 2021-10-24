'''
# notes
아기상어 처음 크기 2
자기보다 큰 물고기가 있는 칸은 못지나감
자기보다 작은 물고기는 먹음. 크기는 1 증가.
가까운 물고기, (r,c) 작은 물고기 순으로 먹음.



# io
n
mtrx

아기상어 이동 몇초?

# strategy
먹을수있는 물고기가 있는지 bfs로 찾아봐야 함. (거리 가까워야 하기 때문) => r,c 리턴
다 찾아봐도 없으면 그 때 리턴
그리고 가는 경로를 기록해둬야 함. => 방문하는 경로리스트를 큐에 넣어야하나? 일단 그렇게 해보자.

bfs 자체에서는..
경로기록과 함께 크기기록도 해야함.
그리고 visit_t는 어떻게 선언할까.. 그때그때 매개변수로 넘겨주는 것밖엔 없을까? 그 땐 deepcopy 써서 복잡해질 것 같은데?
나동빈은 어떻게 풀었나 보자.
함수 두 번 돌려가지고, 푼 것으로 확인된다.

그러네.. 멀리 있다는건 같은 크기에 둘러싸였을때 되는 거구나.
근데 만약에 경로를 저장해야 한다면?

==> 문제를 정말 잘 읽어야한다. 정말정말 놓치는 조건 없이 모든 걸 잘 읽어야 한다.
나중에 디버깅을 할 때도 처음에 잘 읽어놓은 게 훨씬 유리하다.
상식으로 풀지 말고, 항상 의심하고 검증하자.


# pseudo code

'''
import sys
from collections import deque

BLANK = 0
SHARK = 9

n = int(input())
mtrx = [list(map(int, input().split())) for _ in range(n)]
shr, shc = 0, 0

for r in range(n):
    for c in range(n):
        if mtrx[r][c] == SHARK:
            shr, shc = r, c
            mtrx[shr][shc] = BLANK
            break

answer = 0
size = 2

ds = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(shr, shc, size):
    depth_t = [[-1] * n for _ in range(n)]
    depth_t[shr][shc] = 0
    q = deque([(shr, shc)])
    while q:
        r, c = q.popleft()
        depth = depth_t[r][c]
        for dr, dc in ds:
            newr, newc, newdepth = r + dr, c + dc, depth + 1
            # 범위 안에 있니
            if 0 <= newr < n and 0 <= newc < n:
                # 아직 방문 안했으면서, 방문가능하다면 방문
                if depth_t[newr][newc] == -1 and mtrx[newr][newc] <= size:
                    depth_t[newr][newc] = newdepth
                    q.append((newr, newc))

    # print(depth_t)
    target_r, target_c, target_depth = 0, 0, sys.maxsize
    for r in range(n):
        for c in range(n):
            # 피쉬가 있으면서, 갱신가능할때 갱신
            if depth_t[r][c] != -1 and 1 <= mtrx[r][c] < size and depth_t[r][c] < target_depth:
                target_depth = depth_t[r][c]
                target_r, target_c = r, c

    return target_r, target_c, target_depth


eat_n = 0
while True:
    # print(shr, shc, size)
    r, c, depth = bfs(shr, shc, size)
    # print(r, c, depth)
    if depth == sys.maxsize:
        print(answer)
        break
    shr, shc = r, c
    answer += depth
    mtrx[r][c] = BLANK
    eat_n += 1
    if eat_n == size:
        eat_n = 0
        size += 1
