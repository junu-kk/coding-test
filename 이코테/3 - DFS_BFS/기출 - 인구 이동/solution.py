size, low_b, high_b = map(int, input().split())

jido = [list(map(int, input().split())) for _ in range(size)]
group_t = [[-1]*size for _ in range(size)]
group_number = 0


def harm(r, c, group_number):
    global size, low_b, high_b
    print(r, c)
    print(jido)
    if r+1 < size and low_b <= abs(jido[r+1][c]-jido[r][c]) <= high_b:
        group_t[r][c] = group_number
        group_number[r+1][c] = group_number
        harm(r+1, c, group_number)
    if c+1 < size and low_b <= abs(jido[r][c+1]-jido[r][c]) <= high_b:
        group_t[r][c] = group_number
        group_number[r][c+1] = group_number
        harm(r, c+1, group_number)


for r in range(size):
    for c in range(size):
        if group_t[r][c] == -1:
            harm(r, c, group_number)
            group_number += 1

print(group_t)
