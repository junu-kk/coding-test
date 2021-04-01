def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split()) # 노드 & 간선
parent = [0] * (n+1)

edges = []
result = 0 # 

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() # cost 오름차순으로 정렬
total = 0 # total은 모든 edge가중치를 합친 값

# 크루스칼 : 오름차순 edge에서 루트가 다르면 합치는 것. 생각보다 쉽다.

for edge in edges: # 각 edge마다
    cost, a, b = edge
    total += cost
    if find_parent(parent ,a) != find_parent(parent, b): # 루트가 다르면
        union_parent(parent, a, b) # 합치면 됨.
        result += cost

print(total - result)