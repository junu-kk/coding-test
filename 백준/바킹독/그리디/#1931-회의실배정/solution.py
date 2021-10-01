from heapq import heappush, heappop
n = int(input())
h = []
for _ in range(n):
    st, end = map(int, input().split())
    heappush(h, (end, st))

answer = 0
t = 0
while h:
    end, st = heappop(h)
    if st >= t:
        answer += 1
        t = end

print(answer)