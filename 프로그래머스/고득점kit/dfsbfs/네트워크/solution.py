from pprint import pprint


def find_root(parent_t, v):
    if v != parent_t[v]:
        parent_t[v] = find_root(parent_t, parent_t[v])
    return parent_t[v]

def union_vs(parent_t, v1, v2):
    # 더 작은게 parent
    root_v1 = find_root(parent_t, v1)
    root_v2 = find_root(parent_t, v2)
    if root_v1 <= root_v2:
        parent_t[root_v2] = root_v1
    else:
        parent_t[root_v1] = root_v2
        
def solution(vn, computers):
    es = set()
    for r in range(vn):
        for c in range(vn):
            if computers[r][c] == 1:
                if r == c:
                    continue

                if (r, c) in es or (c,r) in es:
                    continue

                es.add((r,c))

    parent_t = [i for i in range(vn)]
    for v1, v2 in es:
        union_vs(parent_t, v1, v2)

    for i in range(vn):
        parent_t[i] = find_root(parent_t, parent_t[i])

    return len(set(parent_t))



    

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
