def find_parent(parent, x): # x의 부모를 찾아 떠나는 함수
    if parent[x] != x: # 루트노드 찾을때까지 재귀 재귀 재귀 ...
        return find_parent(parent, parent[x])
    return x

# 경로압축기법 -> 시간복잡도 개선
def better_find_parent(parent, x):
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

for _ in range(en):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end='')
for i in range(1, vn+1): # 결국 부모만 보일 것임. 1 1 1 1 5 5 이런 식으로. 여기에 추가 응용을 할 수 있겠다.
    print(find_parent(parent, i), end=' ')

print()
print('부모 테이블 : ', end='') # 의미가 있나? 싶지만 단순 부모 테이블 출력
for i in range(1, vn+1):
    print(parent[i], end=' ')