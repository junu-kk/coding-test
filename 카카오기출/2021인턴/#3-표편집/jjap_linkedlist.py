MX = 1200005
dat = pre = nxt = [-1] * MX
unused = 1

num2idx = [-1] * 1000005


def insert(addr: int, num: int):
    global unused
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1
    return unused - 1


def erase(addr: int):
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
        return nxt[addr]
    return pre[addr]


def solution(n, k, cmds):
    for i in range(n):
        num2idx[i] = insert(i, i)
    cur = num2idx[k]
    s = []
    for cmd in cmds:
        if cmd[0] == 'U':
            num = int(cmd.split()[1])
            for _ in range(num):
                cur = pre[cur]
        elif cmd[0] == 'D':
            num = int(cmd.split()[1])
            for _ in range(num):
                cur = nxt[cur]
        elif cmd[0] == 'C':
            s.append((dat[pre[cur]], dat[cur]))
            cur = erase(cur)
        elif cmd[0] == 'Z':
            pre_v, cur_v = s.pop()
            if pre_v == -1:
                pre_i = 0
            else:
                pre_i = num2idx[pre_v]
            num2idx[cur_v] = insert(pre_i, cur_v)
