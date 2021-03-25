from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

prefix_sum = 0
prefix_sums = [0]
for i in nums:
    prefix_sum += i
    prefix_sums.append(prefix_sum)


def get_sum(lo, ro):
    return prefix_sums[ro]-prefix_sums[lo-1]


print(get_sum(1, 1), get_sum(2, 2), get_sum(
    3, 3), get_sum(4, 4), get_sum(5, 5))
print(get_sum(1, 2), get_sum(2, 3), get_sum(3, 4), get_sum(4, 5))
print(get_sum(1, 3), get_sum(2, 4), get_sum(3, 5))
print(get_sum(1, 4), get_sum(2, 5))
print(get_sum(1, 5))
