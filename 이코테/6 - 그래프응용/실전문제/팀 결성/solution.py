from sys import stdin
input = stdin.readline

CMD_UNION = 0
CMD_CMPR_ROOT = 1


def find_root(root_t, v):
    if root_t[v] != v:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_vs(parent_t, v1, v2):
    v1 = find_root(parent_t, v1)
    v2 = find_root(parent_t, v2)
    if v1 < v2:
        parent_t[v2] = v1
    else:
        parent_t[v1] = v2


vn, cmd_n = map(int, input().split())
vn += 1
parent_t = [i for i in range(vn)]

for _ in range(cmd_n):
    cmd, v1, v2 = map(int, input().split())
    if cmd == CMD_UNION:
        union_vs(parent_t, v1, v2)
    elif cmd == CMD_CMPR_ROOT:
        if find_root(parent_t, v1) == find_root(parent_t, v2):
            print('YES')
        else:
            print('NO')
