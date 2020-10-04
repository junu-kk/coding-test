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

es = []
answer = 0

for _ in range(en):
    a, b, cost = map(int, input().split())
    es.append((cost, a, b))

for e in sorted(es): # 사실상 메인코드부분. 각 edge에 대해(거리 오름차순으로)
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b): # 두 점의 부모를 거슬러 올라가, 같지 않다면
        union_parent(parent, a, b) # mst 다리 하나 이어주고
        answer += cost # 거리 더해주고.

print(answer)