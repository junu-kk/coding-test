# 서로소집합 문제구나~ -> 앞쪽 코드는 똑같다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

# 여기까진 똑같고

# 사실 이 부분도 op에 따라 union_parent, find_parent 적용하는거라 똑같다.
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('yes')
        else:
            print('no')