from sys import stdin
input = stdin.readline

N = int(input())
cmds = input().split()
r = 1
c = 1
cmd_d = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}


def good_to_go(d):
    global r, c
    if 1 <= r+d[0] <= N and 1 <= c+d[1] <= N:
        return True
    else:
        return False


for cmd in cmds:
    d = cmd_d[cmd]
    if good_to_go(d):
        r += d[0]
        c += d[1]

print(r, c)
