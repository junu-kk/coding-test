from sys import stdin
input = stdin.readline


def find_root(root_t, v):
    if v != root_t[v]:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_vs(parent_t, v1, v2):
    v1 = find_root(parent_t, v1)
    v2 = find_root(parent_t, v2)

    if v1 < v2:
        parent_t[v2] = v1
    else:
        parent_t[v1] = v2


vn, en = map(int, input().split())
es = sorted([tuple(map(int, input().split()))
             for _ in range(en)], key=lambda x: x[2])
answer = 0
parent_t = [i for i in range(vn+1)]

for e in es:
    v1, v2, dist = e
    if find_root(parent_t, v1) != find_root(parent_t, v2):
        answer += dist
        union_vs(parent_t, v1, v2)

print(answer)
