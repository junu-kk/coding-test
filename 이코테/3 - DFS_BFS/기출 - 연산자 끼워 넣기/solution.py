from itertools import permutations
INF = int(1e9)
max_v = -INF
min_v = INF
n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
op1, op2, op3, op4 = map(int, input().rstrip().split())

ops = []
for _ in range(op1):
    ops.append('+')
for _ in range(op2):
    ops.append('-')
for _ in range(op3):
    ops.append('*')
for _ in range(op4):
    ops.append('/')

zipnums = nums[1:]
for perm in permutations(ops):
    result = nums[0]
    for num, op in zip(zipnums, perm):
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if result >= 0:
                result //= num
            else:
                result = -((-result) // num)
    max_v = max(max_v, result)
    min_v = min(min_v, result)
    
print(max_v)
print(min_v)