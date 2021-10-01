'''
# io
5
1 1 1 6 0 -> 재배열 하며
2 7 8 3 1 -> 재배열 없이

18 -> 만들 수 있는 가장 큰 수

# notes
주어지는 수들 모두 0 이상

# strategy
당연히.. 높은 수랑 높은 걸 곱하는게 젤 좋겠다는 생각이 든다.
아 최댓값이 아니구나 최솟값을 찾는 경우라면
b의 높은수랑 a의 낮은수를 곱하면 되겠다.

# pseudo code
둘 다 최대힙으로 받고
하나씩 팝해주며 계산해나가면 됨.

'''
from heapq import heappush, heappop

n = int(input())
al = list(map(int, input().split()))
h1 = []
for a in al:
    heappush(h1, a)
h2 = []
bl = list(map(int, input().split()))
h2 = []
for b in bl:
    heappush(h2, -b)

answer = 0
for _ in range(n):
    answer += heappop(h1) * -heappop(h2)

print(answer)