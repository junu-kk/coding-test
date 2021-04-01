from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

n = int(input())
q = []
for _ in range(n):
    name, kor, eng, math = input().split()
    heappush(q, (-int(kor), int(eng), -int(math), name))
for _ in range(n):
    print(heappop(q)[3])
