from collections import deque

from sys import stdin
input = stdin.readline

BLANK = 0
APPLE = 1
U, R, D, L = range(4)
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


jido_l = int(input())
jido = [[BLANK]*jido_l for _ in range(jido_l)]

apple_n = int(input())
for _ in range(apple_n):
    r, c = map(int, input().split())
    jido[r-1][c-1] = APPLE

cmd_n = int(input())
cmds = deque()
for _ in range(cmd_n):  # 큐를 활용할까?
    time, cmd = input().split()
    cmds.append((int(time), cmd))
cmds.append((0, 0))  # 마지막에 오류뜨지 않게 잉여 튜플 하나 더 넣어줌.

locs = deque([(0, 0)])
d = R


def does_collide(r, c):
    if 0 <= r < jido_l and 0 <= c < jido_l:  # 지도에 있는가
        if (r, c) not in locs:  # 뱀이랑 부딪히지 않는가
            return False
    return True


cmd_time, cmd = cmds.popleft()
time = 0
while True:
    time += 1
    r, c = locs[-1]
    dr, dc = ds[d]
    if does_collide(r+dr, c+dc):
        break
    # 사과면 popleft 안해줘도 됨.
    locs.append((r+dr, c+dc))
    if jido[r+dr][c+dc] == BLANK:
        locs.popleft()
    # 처리 후
    if time == cmd_time:
        if cmd == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4
        cmd_time, cmd = cmds.popleft()

print(time)
