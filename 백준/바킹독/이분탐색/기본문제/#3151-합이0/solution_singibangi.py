'''
아이디어는 비슷했고,
하나를 잡고 그 합이 있는지 이분탐색으로 확인하는 방법으로.


'''
from sys import stdin

input = stdin.readline

n = int(input())
nums = map(int, input().split())
answer = 0
cnt = [0] * 40001

for i in range(n):
    num = nums[i]
    answer += cnt[20000 - num]  # 인덱스 20000~0까지 num은 0~20000이 할당된다.
    for j in range(i):
        cnt[20000 + num + nums[j]] += 1
print(answer)

print(answer)
