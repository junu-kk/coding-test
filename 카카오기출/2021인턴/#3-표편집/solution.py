# INF = int(1e9)
MX = 1200005  # n + len(cmds) + 더미 다섯개
UNUSED = -1
pre = [UNUSED] * MX
nxt = [UNUSED] * MX


def solution(n, k, cmds):
    answer = ['O'] * n
    for i in range(n):
        pre[i], nxt[i] = i - 1, i + 1
    nxt[n - 1] = -1
    cur = k
    s = []
    for cmd in cmds:
        if cmd[0] == 'U':
            mv_cnt = int(cmd.split()[1])
            for _ in range(mv_cnt):
                cur = pre[cur]
        elif cmd[0] == 'D':
            mv_cnt = int(cmd.split()[1])
            for _ in range(mv_cnt):
                cur = nxt[cur]
        elif cmd[0] == 'C':
            s.append((pre[cur], cur, nxt[cur]))
            if pre[cur] != UNUSED:
                nxt[pre[cur]] = nxt[cur]
            if nxt[cur] != UNUSED:
                pre[nxt[cur]] = pre[cur]
            answer[cur] = 'X'

            if nxt[cur] != UNUSED:
                cur = nxt[cur]
            else:
                cur = pre[cur]

        elif cmd[0] == 'Z':
            pre_i, ret_i, nxt_i = s.pop()
            if pre_i != UNUSED:
                nxt[pre_i] = ret_i
            if nxt_i != UNUSED:
                pre[nxt_i] = ret_i
            answer[ret_i] = 'O'

    return ''.join(answer)


print(solution())
