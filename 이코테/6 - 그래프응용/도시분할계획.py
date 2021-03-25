'''
문제에서 알수있는것.
무방향 가중치
두개의 mst -> mst 문제인데, 거기서 가장 비용큰 간선 빼면 두개의 마을로 나뉘어진다.
'''
# 역시나 앞쪽은 똑같고
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

vn, en = map(int, input().split())
es = []
result = 0
parent = [0] * (vn+1)

for i in range(0, vn+1):
    parent[i] = i

for _ in range(en):
    a, b, cost = map(int, input().split())
    es.append((cost, a, b))

last = 0 # 가장 비용 큰 간선. 나중에 result에서 이거 뺄 계획. 근데 어차피 가중치 순서대로 가니까 젤 마지막거가 되겠지.

for e in sorted(es):
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)