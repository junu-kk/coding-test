from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

n = int(input().rstrip())
q = []
for _ in range(n):
    heappush(q, int(input().rstrip()))

answer = 0
for _ in range(n-1):
    c1 = heappop(q)
    c2 = heappop(q)
    answer += c1+c2
    heappush(q, c1+c2)

print(answer)
