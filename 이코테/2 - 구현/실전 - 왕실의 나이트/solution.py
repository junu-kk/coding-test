from sys import stdin
input = stdin.readline

ds = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

loc = input()
r = ord(loc[0]) - ord('a') + 1
c = int(loc[1])
answer = 0
for d in ds:
    if 1 <= r+d[0] <= 8 and 1 <= c+d[1] <= 8:
        answer += 1

print(answer)
