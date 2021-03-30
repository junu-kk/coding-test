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
