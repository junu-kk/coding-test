'''
# notes
상어들이 있다.
1~m의 번호를 갖고 있음. 번호 낮을수록 셈.

냄새를 뿌린다 (상어 k번 이동 후 사라짐)
상어가 이동한다 (우선순위 방향 따름)
    냄새없는 칸 우선
    자기냄새 칸
    겹치기 가능.
겹치는 상어가 있다면 가장 작은번호가 다 먹어버린다.

1번 상어만 격자에 남게 되기까지 몇 초가 걸리는가?



# io
n, shark_n, smell_t
mtrx
dis
1번상어 상하좌우 우선순위
...
shark_n번상어 상하좌우 우선순위

# strategy
smell_t
shark_t

# pseudo code

'''
from copy import deepcopy


class Smell:
    def __init__(self, shi, t):
        self.shi = shi
        self.t = t


n, shark_n, smell_t = map(int, input().split())
shark_t = [list(map(int, input().split())) for _ in range(n)]

dis = list(map(int, input().split()))

smell_t = [[Smell(0, 0)] * n for _ in range(n)]
pris = [[] for _ in range(shark_n)]
for i in range(shark_n):
    for _ in range(4):
        pris[i].append(list(map(int, input().split())))

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0
while True:
    # 냄새뿌리기
    for r in range(n):
        for c in range(n):
            shark = shark_t[r][c]
            smell = smell_t[r][c]
            if smell.t > 0:
                smell.t -= 1
            if shark != 0:
                smell_t[r][c] = Smell(shark, smell_t)

    # 상어 이동
    new_sht = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            shark = shark_t[r][c]
            smell = smell_t[r][c]
            if shark != 0:
                sh_di = dis[shark-1]
                found = False
                for idx in range(4):
                    ...