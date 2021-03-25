from sys import stdin
input = stdin.readline

bn, cn = map(int, input().split())
bs = list(map(int, input().split()))
cs = list(map(int, input().split()))

answer = [0]*(bn+cn)
bi, ci, ans_i = 0, 0, 0

while bi < bn or ci < cn:
    if ci >= cn or (bi < bn and bs[bi] <= cs[ci]):
        answer[ans_i] = bs[bi]
        bi += 1
    else:
        answer[ans_i] = cs[ci]
        ci += 1
    ans_i += 1

print(answer)
