from sys import stdin
input = stdin.readline

n = int(input().rstrip())
jido = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp_t = [[0]*(i+1) for i in range(n)]

dp_t[0][0] = jido[0][0]
for r in range(1, n):  # r는 인덱스 1부터 n-1까지
    dp_t[r][0] = dp_t[r-1][0] + jido[r][0]
    for c in range(1, r):  # c는 인덱스 0부터 r까지
        dp_t[r][c] = max(dp_t[r-1][c], dp_t[r-1][c-1])+jido[r][c]
    dp_t[r][r] = dp_t[r-1][r-1] + jido[r][r]

print(max(dp_t[n-1]))
