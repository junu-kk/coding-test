from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
target_sum = int(input())

answer = 0
part_sum = 0
ri = 0

for li in range(n):
    while part_sum < target_sum and ri < n:
        part_sum += nums[ri]
        ri += 1
    if part_sum == target_sum:
        answer += 1
    part_sum -= nums[li]

print(answer)
