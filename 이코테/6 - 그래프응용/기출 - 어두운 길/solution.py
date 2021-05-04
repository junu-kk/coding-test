def find_root(root_t, v):
    if root_t[v] != v:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_parent(parent_t, v1, v2):
    r1 = find_root(parent_t, v1)
    r2 = find_root(parent_t, v2)
    if r1 < r2:
        parent_t[r2] = r1
    elif r1 > r2:
        parent_t[r1] = r2


while True:
    vn, en = map(int, input().split())
    if vn == 0 and en == 0:
        break
    es = []
    answer = 0
    for _ in range(en):
        e = tuple(map(int, input().split()))
        es.append(e)
        answer += e[2]
    es.sort(key=lambda x: x[2])  # cost 오름차순 정렬
    parent_t = [i for i in range(vn)]
    for e in es:
        v1, v2, cost = e
        if find_root(parent_t, v1) != find_root(parent_t, v2):
            union_parent(parent_t, v1, v2)
            answer -= cost

    print(answer)
