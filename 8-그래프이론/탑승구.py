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

g = int(input())
p = int(input())
parent = [0] * (g+1) # 신기하네.. 리스트는 이렇게 선언해도 자동 전역인게.

for i in range(1, g+1):
    parent[i] = i

result = 0
planes = []
for _ in range(p):
    planes.append(int(input()))

for plane in planes:
    data = find_parent(parent, plane)
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result += 1

print(result)