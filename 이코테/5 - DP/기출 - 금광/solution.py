from sys import stdin
input = stdin.readline

tc_n = int(input())
for tc in range(tc_n):
    rn, cn = map(int, input().split())
    jido = [[0]*cn for _ in range(rn)]
    nums = list(map(int, input().split()))
    for i in range(rn*cn):
        r, c = divmod(i, cn)
        jido[r][c] = nums[i]
    dp_t = [[0]*cn for _ in range(rn)]
    for r in range(rn):
        dp_t[r][0] = jido[r][0]
    for c in range(1, cn):
        for r in range(rn):
            plusing = dp_t[r][c-1]
            if r > 0:
                plusing = max(plusing, dp_t[r-1][c-1])
            if r < rn-1:
                plusing = max(plusing, dp_t[r+1][c-1])
            dp_t[r][c] = jido[r][c] + plusing

    print(max([row[-1] for row in dp_t]))
