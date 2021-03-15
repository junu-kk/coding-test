from itertools import permutations
from sys import stdin
input = stdin.readline

max_v = int(-1e9)
min_v = int(1e9)

n = int(input())
nums = list(map(int, input().split()))
op_ns = list(map(int, input().split()))
ops = ''
ops += '+' * op_ns[0]
ops += '-' * op_ns[1]
ops += '*' * op_ns[2]
ops += '/' * op_ns[3]

op_cases = permutations(ops, n-1)
for op_case in op_cases:
    result = nums[0]
    for num, op in zip(nums[1:], op_case):
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if result < 0:
                result = -((-result) // num)
            else:
                result //= num

    if result > max_v:
        max_v = result
    if result < min_v:
        min_v = result

print(max_v)
print(min_v)


###### 디버깅용 ######
# nums = [1, 2, 3, 4, 5, 6]
# op_case = ('-', '/', '+', '+', '*')
# result = nums[0]
# for num, op in zip(nums[1:], op_case):
#     if op == '+':
#         result += num
#     elif op == '-':
#         result -= num
#     elif op == '*':
#         result *= num
#     elif op == '/':
#         if result < 0:
#             result = -((-result) // num)
#         else:
#             result //= num
#     print(result)
