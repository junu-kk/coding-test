##### 앞쪽은 서로소집합과 같음. #####

# 경로압축기법 -> 시간복잡도 개선
def find_parent(parent, x):
    if parent[x] != x: # 부모를 끝까지 갈때까지 갱신시키기. 역시 재귀 활용.
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # a와 b를 union해주는 함수
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # 큰게 작은걸 가리키도록. 즉 작은게 부모.
        parent[b] = a
    else:
        parent[a] = b

vn, en = map(int, input().split())
parent = [0] * (vn+1)

for i in range(1, vn+1):
    parent[i] = i # 부모테이블 초기세팅 : 자기 부모는 자신

##### 앞쪽은 서로소집합과 같음. #####

cycle = False

for i in range(en):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b): # 부모가 같다? 싸이클이네!
        cycle = True # 더 돌것 없이 바로 싸이클트루브레이크
        break
    else: # 부모 다르면 그냥 union 연산 수행
        union_parent(parent, a, b)

if cycle:
    print('사이클 ㅇㅇ')
else:
    print('사이클 ㄴㄴ')