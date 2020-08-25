n = int(input())
dirs = input().split()

class Man:
    def __init__(self):
        self.r = 1
        self.c = 1

man = Man()
# 시계방향이 좋아.
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

for d in dirs:
    if d == 'U':
        if man.r != 1:
            man.r -= 1
    elif d == 'R':
        if man.c != n:
            man.c += 1
    elif d == 'D':
        if man.r != n:
            man.r += 1
    elif d == 'L':
        if man.c != 1:
            man.c -= 1

print(man.r, man.c)