from itertools import combinations


def find_root(root_t, v):
    if root_t[v] != v:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_parent(parent_t, v1, v2):
    r1 = find_root(parent_t, v1)
    r2 = find_root(parent_t, v2)
    if r1 < r2:
        parent_t[r2] = r1
    elif r2 < r1:
        parent_t[r1] = r2


def get_cost(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return min(abs(x1-x2), abs(y1-y2), abs(z1-z2))


vn = int(input())
vs = [tuple(map(int, input().split())) for _ in range(vn)]
es = []

for v_comb in combinations(range(vn), 2):
    v1_idx, v2_idx = v_comb
    v1 = vs[v1_idx]
    v2 = vs[v2_idx]
    es.append((v1_idx, v2_idx, get_cost(v1, v2)))

es.sort(key=lambda x: x[2])  # cost 오름차순 소트
parent_t = [i for i in range(vn)]
answer = 0
for e in es:
    # print(e)
    v1, v2, cost = e
    if find_root(parent_t, v1) != find_root(parent_t, v2):
        union_parent(parent_t, v1, v2)
        answer += cost

print(answer)
