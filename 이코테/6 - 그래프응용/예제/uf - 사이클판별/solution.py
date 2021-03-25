from ..uf import find_root, union_vs
from sys import stdin
input = stdin.readline


vn, en = map(int, input().split())
parent_t = [i for i in range(vn+1)]
cycle = False
for _ in range(en):
    v1, v2 = map(int, input().split())
    if find_root(parent_t, v1) == find_root(parent_t, v2):
        cycle = True
        break
    else:
        union_vs(parent_t, v1, v2)

print(cycle)
