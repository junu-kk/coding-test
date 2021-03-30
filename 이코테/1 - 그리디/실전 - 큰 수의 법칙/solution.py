from sys import stdin
input = stdin.readline

_, n, max_combo = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

max1, max2 = nums[0], nums[1]

q = n // (max_combo+1)
r = n % (max_combo+1)

answer = (max1*max_combo + max2) * q + max1 * r
print(answer)
