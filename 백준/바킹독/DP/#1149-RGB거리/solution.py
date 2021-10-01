'''
# io
3 # 집 개수
26 40 83 # 1번집 rgb당 요금
49 60 57 # 2번집
13 89 99 # 3번집

96 # rbr이 가장 싸게 먹힘.

# notes


# strategy
역시 dp를 써야할것같긴한데..
아까의 아이디어를 한 번 더 이용한다면, rgb 중 어떤 곳을 기록했는지까지 해서 dp_t를 만들면 될 것 같다.
dp_t[n][색깔] : n번 집까지의 누적요금 최솟값. 현 집은 해당 색깔로 칠했다고 가정.

# pseudo code



'''
n = int(input())
dp_t = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    dp_t[i][0] = r + min(dp_t[i-1][1], dp_t[i-1][2])
    dp_t[i][1] = g + min(dp_t[i-1][0], dp_t[i-1][2])
    dp_t[i][2] = b + min(dp_t[i-1][0], dp_t[i-1][1])

print(min(dp_t[n]))
