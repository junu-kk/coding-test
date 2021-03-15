import sys
input = sys.stdin.readline

# 오.. 방향벡터를 먼저 설정해줬구나.
# 나중에 인덱스로 접근하기 편하게 해줬네.
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
a = [[0]*101 for _ in range(101)]  # 맵을 먼저 설정해줌. 1이면 지나가는거 0이면 안지나가는거.
for _ in range(n):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1  # 당연히 시작점은 지나갈 테고

    ###### 움직이는 방향을 쫙 쌓아놓은 뒤 ######
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):  # 움직이는 방향의 개수만큼
            temp.append((move[-i-1] + 1) % 4)  # reverse + 1 적용.
        move.extend(temp)  # extend는 concat이라고 생각하면 됨.

    ###### 해당 움직임에 따른 map을 변화시킴  ######
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        a[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if a[i][j]:
            if a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
                ans += 1
print(ans)
