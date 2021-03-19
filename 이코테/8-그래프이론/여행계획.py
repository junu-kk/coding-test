parent = [0] * (n+1) # parent는 전역으로 선언해야지.

def find_parent(parent, x): # 본인이 소속된 곳의 루트찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 합치기 (루트찾아 합치기)
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split()) # 여행지 n개 도시 m개

for i in range(1, n+1): # 일단 독립적으로, 내 부모는 나로 추기화.
    parent[i] = i

for i in range(n): # 일단 그래프 입력을 받을텐데
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 이어져있는거 발견하면
            union_parent(parent, i+1, j+1) # 그룹묶기

plan = list(map(int, input().split())) # 탐방계획 입력받고
result = True

for i in range(m-1): # 슉슉 넘어갈 때 같은 그룹에 속해있지 않는다면 False 리턴
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
        break

print('YES' if result else 'NO')