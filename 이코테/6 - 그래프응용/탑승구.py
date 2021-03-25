def find_parent(parent, x): # 기존 코드와 똑같으니
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 설명은 생략
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input()) # number of gates
p = int(input()) # number of planes

parent = [0] * (g+1) # 신기하네.. 리스트는 이렇게 선언해도 자동 전역인게.

for i in range(1, g+1):
    parent[i] = i

result = 0
planes = []
for _ in range(p):
    planes.append(int(input()))

for plane in planes:
    data = find_parent(parent, plane)
    if data == 0: # 0에 다다르면 더 이상 주차할 데가 없다는 뜻.
        break
    union_parent(parent, data, data-1) # data 자리에 주차하면 
    result += 1

print(result)