from sys import stdin
input = stdin.readline
INF = int(1e9)

rn, cn = map(int, input().split())
answer = -INF

for _ in range(rn):
    min_v = min(list(map(int, input().split())))
    if min_v > answer:  # max 함수로 대체가능하구나!
        answer = min_v

print(answer)
