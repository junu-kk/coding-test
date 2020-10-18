# 꼭 나중에 다시 한 번 구현해보자.
# 정말 충실히 구현하면 되긴 할듯.

n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x, y = 1, 1
    graph[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        newx = x + dx[direction]
        newy = y + dy[direction]
        if 1 <= newx <= n and 1 <= newy <= n and graph[newx][newy] != 2:
            if graph[newx][newy] == 0:
                graph[newx][newy] = 2
                q.append((newx, newy))
                prevx, prevy = q.pop(0)
                graph[prevx][prevy] = 0
            if graph[newx][newy] == 1:
                graph[newx][newy] = 2
                q.append((newx, newy))
        else:
            time += 1
            break
        x, y = newx, newy
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())



'''
====input====
N(보드크기)
K(사과개수)
사과위치
사과위치
...
L(뱀의방향변환정보)
언제 어느방향으로
언제 어느방향으로
...
맨좌측에서 오른쪽 향하는 뱀

ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅅㅁ
ㅁㅁㅁㅅㅁㅁ
ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅅㅁㅁㅁ
ㅁㅁㅁㅁㅁㅁ

====output====
게임끝나는 시간

음... 진짜 말그대로 구현을 하면 되는 문제인 것 같긴 한데
쉽지 않아보인다.
정답코드 봐야할듯 ㅜㅜ

'''