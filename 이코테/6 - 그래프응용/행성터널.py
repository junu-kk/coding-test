# edge를 x, y, z 나눠 일일이 비교하게 되면 시간초과 뜸.
# 그래서 x로만, y로만, z로만 해서 거리 오름차순으로 구한다음에
# 그 세개를 가지고 짬뽕해 크루스칼 적용.

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

n = int(input())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

# 여기까진 똑같.

# 각 좌표 모음
x = []
y = []
z = []

for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i)) # 비용과 노드번호.
    y.append((data[1], i))
    z.append((data[2], i))

x.sort(); y.sort(); z.sort() # x, y, z 각각의 비용순 정렬까지 완료.

for i in range(n-1):
    '''
    비용 : 거리1, 거리2, 거리3, ...
    시작점&끝점 : 0-1 1-2 2-3 ...
    '''
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1])) # 비용, 시작점, 끝점
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort() # 한번 더 비용순으로 정렬 해주고

for edge in edges: # x y z가 뒤섞인 edge들에 대해
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b): # 크루스칼 적용.
        union_parent(parent, a, b)
        result += cost

print(result)