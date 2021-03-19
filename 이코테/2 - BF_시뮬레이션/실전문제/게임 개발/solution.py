from sys import is_finalizing, stdin
input = stdin.readline

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rn, cn = map(int, input().split())
r, c, d = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(rn)]
jido[r][c] = 2  # 처음에 밟은 땅 방문찍고
answer = 1  # 처음에 밟은 땅은 1칸


def is_in_map(r, c):
    global rn, cn
    if 0 <= r < rn and 0 <= c < cn:
        return True
    return False


while True:
    for _ in range(4):
        d = (d-1) % 4
        dr, dc = ds[d]
        if is_in_map(r+dr, c+dc) and jido[r+dr][c+dc] == 0:
            r += dr  # 움직이고
            c += dc
            jido[r][c] = 2  # 방문 찍고
            answer += 1
            break
    # 여기까지 온 경우는 사방이 1 혹은 2인 경우임. 방향은 처음 그대로겠지.
    else:  # for-else문 사용!
        if is_in_map(r-dr, c-dc) and jido[r-dr][c-dc] == 2:
            r -= dr
            c -= dc
        else:
            break

print(answer)
