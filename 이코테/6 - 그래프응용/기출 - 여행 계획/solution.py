def find_root(root_t, v):
    if root_t[v] != v:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_parent(parent_t, v1, v2):
    p1, p2 = find_root(parent_t, v1), find_root(parent_t, v2)
    if p1 < p2:
        parent_t[p2] = p1
    else:
        parent_t[p1] = p2


def solution():
    vn, _ = map(int, input().split())
    jido = [list(map(int, input().split())) for _ in range(vn)]
    parent_t = [i for i in range(vn+1)]
    for r in range(vn):
        for c in range(vn):
            if jido[r][c]:
                union_parent(parent_t, r, c)
    travel_vs = list(set(map(int, input().split())))
    root = find_root(parent_t, travel_vs[0])
    for travel_v in travel_vs[1:]:
        if root != find_root(parent_t, travel_v):
            print('NO')
            return
    print('YES')


solution()
