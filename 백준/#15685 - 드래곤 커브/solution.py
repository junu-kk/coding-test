'''
풀이 참조
https://chldkato.tistory.com/150
https://yeoping.tistory.com/29

<개선할점>
1. 맵에 기록하는 것
처음에 범위를 보고 전체 맵을 0으로 잡은 다음에,
꼭짓점이 지나갈 때 해당 부분을 1로 바꾸는 건 내가 하지 못했던 생각이다.
지도 문제에서, 범위가 주어져 있으면 적극 활용해야겠다.


2. 방향벡터
여기서 방향벡터가 쓰일 줄은 몰랐는데,
0 1 2 3에서 힌트를 얻을 수 있었던 것 같다.
사실 여기서 3번의 바로 꼭짓점이 아닌 방향을 통한 접근이 나올 수 있었다.


3. 바로 꼭짓점 찾는게아닌 방향을 통한 접근
0세대 : ...
1세대 : ...
에서 나는 꼭짓점을 나열해 접근했었는데
방향을 통해 접근했다면 "그 전 세대의 reverse + 1" 의 규칙을 찾았을 수 있을것이다.
이는 방향을 쫙 구한다음에
차차 풀면 됨.


<개선된점>
규칙성이 안보였을 때 포기하지 않고
종이에 써가면서 찾아보려고 했고
방향은 틀렸지만 그래도 나름의 규칙을 발견했다는 점이 의미있다.
'''

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
