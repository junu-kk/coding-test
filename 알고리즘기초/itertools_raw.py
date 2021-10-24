from itertools import combinations, permutations, combinations_with_replacement as cwr, product
from copy import deepcopy
n, m = map(int, input().split())

print(list(combinations(range(1, n + 1), 2)))
print(list(permutations(range(1, n + 1), 2)))
print(list(cwr(range(1, n + 1), 2)))
print(list(product(range(1, n + 1), repeat=m)))

combs = []
perms = []
products = []
cwrs = []

s = []
visit_t = [False] * n

def raw_comb(depth, n, m):
    if depth == m:
        combs.append(deepcopy(s))
        return

    for i in range(n):
        if visit_t[i]:
            continue

        visit_t[i] = True
        s.append(i+1)

        raw_comb(depth+1, n, m)

        for ti in range(i+1, n):
            visit_t[ti] = False
        s.pop()


def raw_perm(depth, n, m):
    if depth == m:
        perms.append(deepcopy(s))
        return

    for i in range(n):
        if visit_t[i]:
            continue

        # 치고
        visit_t[i] = True
        s.append(i+1)

        # 재귀하고
        raw_perm(depth+1, n, m)

        # 빠진다
        visit_t[i] = False
        s.pop()

def raw_product(depth):
    # visit_t를 아예 신경안쓰는 순수한 백트래킹
    pass

def raw_cwr(depth):
    # combination인데 visit을 늦게 해줌.
    pass


raw_perm(0, n, m)
print(perms)

s.clear()
visit_t = [False] * n

print(visit_t, s)
raw_comb(0, 4, 2)
print(combs)