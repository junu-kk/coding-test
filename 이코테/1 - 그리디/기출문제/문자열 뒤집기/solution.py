nums = input()
digit_n = {'0': 0, '1': 0}
current_digit = nums[0]
digit_n[current_digit] += 1

for i in range(1, len(nums)):
    if nums[i] != current_digit:
        current_digit = nums[i]
        digit_n[current_digit] += 1

print(min(digit_n.values()))
