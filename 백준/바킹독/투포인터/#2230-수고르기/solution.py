'''
<오늘의 교훈>
범위 확인하자. 1e9보다 더 클 수 있다.

<io>
3 3
1
5
3


4

<notes>
두 수를 골랐을 때 차이가 m 이상이면서 가장 작은 경우


<strategy>
1 3 5 후 투포인터로 하면 되겠다.
처음에 i=0, j=0으로 놓고
i<len일때까지 반복:
    m보다 차이가 작으면
        j +=1
    m보다 차이가 크거나 같으면
        min값 갱신
        i += 1

'''
from sys import maxsize
n, m = map(int, input().split())
nums = sorted(int(input()) for _ in range(n))
i, j = 0, 0
answer = int(maxsize)

while j < n and i < n:
    bigger, smaller = nums[j], nums[i]
    chai = bigger - smaller
    if chai >= m:
        answer = min(chai, answer)
        i += 1
    else:
        j += 1


print(answer)
