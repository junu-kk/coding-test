from collections import deque
from sys import stdin
input = stdin.readline

CLEAN = 0

n, virus_n = map(int, input().rstrip().split())
jido = []
viruses = []  # 이게 기존 내 풀이랑 다름. jido만 두는 게 아니라 바이러스를 따로 둠.
for r in range(n):
    jido.append(list(map(int, input().rstrip().split())))
    for c in range(n):
        if jido[r][c] != CLEAN:
            viruses.append((jido[r][c], 0, r, c))  # 번호, 시간, 위치

viruses.sort()
q = deque(viruses)

target_t, target_r, target_c = map(int, input().rstrip().split())
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_in_map(r, c):
    global n
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


while q:
    virus, t, r, c = q.popleft()
    if t == target_t:  # 시간이 다 차게 되었다면 while문 탈출
        break
    for d in ds:
        dr, dc = d
        newr, newc = r+dr, c+dc
        if is_in_map(newr, newc) and jido[newr][newc] == CLEAN:
            jido[newr][newc] = virus
            q.append((virus, t+1, newr, newc))  # 와 이게 좀 신박하다.

print(jido[target_r-1][target_c-1])
