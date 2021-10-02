'''
# io
6 # 총 6층
10
20
15
25
10
20

75 # 6층까지 갔을 때 얻을 수 있는 최대 접수


# notes
- 한칸 or 두칸점프 ㄱㄴ
- 연속3계단 밟아선 안됨.
- 막계단은 당연히 밟아야 함.

# strategy
최대한 계단을 덜 밟는게 중요하겠다.
다만 연속 세개를 안밟는것까지 어떻게 저장하지??
이 문제는 해설을 봐야겠다.

# pseudo code



'''
sn = int(input())
stairs = [0]
for _ in range(sn):
    stairs.append(int(input()))

if sn == 1:
    print(stairs[1])
    exit()

dp_t = [[0] * 3 for _ in range(sn + 1)]  # dp_t[i][j] : i번째 계단 밟을때 최댓값 (연속해서 계단 j개밟음)
dp_t[1][1] = stairs[1]
dp_t[1][2] = 0
dp_t[2][1] = stairs[2]
dp_t[2][2] = stairs[1] + stairs[2]

for i in range(3, sn + 1):
    dp_t[i][1] = max(dp_t[i - 2][1], dp_t[i - 2][2]) + stairs[i]
    dp_t[i][2] = dp_t[i - 1][1] + stairs[i]

print(max(dp_t[sn][1], dp_t[sn][2]))
