import sys

input = sys.stdin.readline

num_n, change_n, sum_n = map(int, input().split())

nums = [0] * (num_n + 1)
tree = [0] * (num_n + 1)


def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result


def update(i, dif):
    while i <= num_n:
        tree[i] += dif
        i += (i & -i)


def interval_sum(st, end):
    return prefix_sum(end) - prefix_sum(st - 1)


for i in range(1, num_n + 1):
    num = int(input())
    nums[i] = num
    update(i, num)

for i in range(change_n + sum_n):
    op, n1, n2 = map(int, input().split())
    if op == 1:  # UPDATE
        dif = n2 - nums[n1]
        update(n1, dif)
        nums[n1] = n2
    elif op == 2:  # INTERVAL_SUM
        print(interval_sum(n1, n2))
