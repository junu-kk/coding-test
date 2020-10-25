import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

answer = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ab = a + b
    heapq.heappush(heap, ab)
    answer += ab

print(answer)