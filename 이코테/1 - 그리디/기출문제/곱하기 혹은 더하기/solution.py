nums = list(map(int, list(input())))
answer = nums[0]
for i in range(1, len(nums)):
    if nums[i] not in (0, 1) and answer not in (0, 1):
        answer *= nums[i]
    else:
        answer += nums[i]

print(answer)
