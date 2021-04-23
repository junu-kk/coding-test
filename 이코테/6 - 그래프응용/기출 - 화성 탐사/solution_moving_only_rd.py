from sys import stdin
input = stdin.readline
INF = int(1e9)

tc_n = int(input().rstrip())
for tc in range(tc_n):
    n = int(input().rstrip())
    jido = [list(map(int, input().rstrip().split())) for _ in range(n)]

    dp_t = [[-1]*(n) for _ in range(n)]
    dp_t[0][0] = jido[0][0]
    for i in range(1, n):
        dp_t[0][i] = dp_t[0][i-1] + jido[0][i]
        dp_t[i][0] = dp_t[i-1][0] + jido[i][0]

    for r in range(1, n):
        for c in range(1, n):
            dp_t[r][c] = min(dp_t[r-1][c], dp_t[r][c-1]) + jido[r][c]

    print(dp_t[n-1][n-1])
