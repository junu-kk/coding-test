# 구현
완전탐색, 시뮬레이션 같은 유형들.  
완전탐색 : 싹 다 계산  
시뮬레이션 : 문제에서 제시한 알고리즘을 직접 수행

## 방향벡터
내 기준 : 12시 3시 6시 9시

```
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
```

상하좌우 문제를 예로 든다면

```
n = int(input())
x, y = 1, 1
plans = input().split()

# 방향벡터와 moves 정의
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
moves = ['U', 'R', 'D', 'L']

# 각 이동마다, 위 정의에 따라 dest_r, dest_c를 설정한 뒤
for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            dest_r = r + dr[i]
            dest_c = c + dc[i]
    
    # 유효하면 ㄱ 아니면 ㄴ
    if dest_r < 1 or dest_c < 1 or dest_r > n or dest_c > n:
        continue
    r, c = nr, nc

print(r, c)
```