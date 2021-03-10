loc = input()
r = ord(loc[0]) - ord('a') + 1
c = int(loc[1])

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
dirs = [1, 2, 4, 5, 7, 8, 10, 11]

answer = 8

for nr, nc in zip(dr, dc):
    dest_r = r + nr
    dest_c = c + nc
    if dest_r < 1 or dest_c < 1 or dest_r > 8 or dest_c > 8:
        answer -= 1

print(answer)