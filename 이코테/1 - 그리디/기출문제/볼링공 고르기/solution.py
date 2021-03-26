from collections import Counter
from sys import stdin
input = stdin.readline

n, max_ball = map(int, input().split())
answer = (n*(n-1))//2
balls = list(map(int, input().split()))
balls_c = Counter(balls)
for ball in balls_c:
    if balls_c[ball] >= 2:
        answer -= (balls_c[ball]*(balls_c[ball]-1))//2

print(answer)
