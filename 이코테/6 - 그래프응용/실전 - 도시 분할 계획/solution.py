from sys import stdin
input = stdin.readline


def find_root(root_t, v):
    if root_t[v] != v:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_vs(parent_t, v1, v2):
    v1 = find_root(parent_t, parent_t[v1])
    v2 = find_root(parent_t, parent_t[v2])
    if v1 < v2:
        parent_t[v2] = v1
    else:
        parent_t[v1] = v2


vn, en = map(int, input().split())
parent_t = [i for i in range(vn+1)]
es = []
for _ in range(en):
    v1, v2, cost = map(int, input().split())
    es.append((cost, v1, v2))

mst_costs = []
for e in sorted(es):
    cost, v1, v2 = e
    if find_root(parent_t, v1) != find_root(parent_t, v2):
        mst_costs.append(cost)
        union_vs(parent_t, v1, v2)

# 오 어차피 mst_costs는 sorted된 상태일 것이다!
print(sum(mst_costs[:-1]))
