# 30 / 40

'''
A, B가 r, c 말하는거임. 다만 (0,0)부터 시작하네.
1. left face
2. 갈 수 잇으면 ㄱ. 없으면 1단계.
3. 막히면 한칸 뒤로 가고 1단계. ㄹㅇ 막히면 끝.

input
- 멥 세로, 가로
- 좌표와 방향
- 맵상태 입력 : 0은육지 1은바다

output
- 방문 칸 수

'''
jido = []
r_n, c_n = map(int, input().split())
r, c, d = map(int, input().split())

# 왼쪽으로 움직이므로 원래 쓰던 방법 살짝 바꾸자.
dr = [0, 1, 0, -1] * 2
dc = [-1, 0, 1, 0] * 2

for _ in range(r_n):
    jido.append(list(map(int, input().split())))

'''
d == 0일때
서 갈데있는가? : 있으면 해당방향 이동.
남 갈데있는가?
동 갈데있는가?
북 갈데있는가?

d == 1일때
남
동
북
서

다 없으면 종료.
'''

# 캐릭터는 jido[r][c]에 있음.
leggo = True
answer = 1

while leggo:
    leggo = False
    for i in range(d, d+4):
        dest_r = r + dr[i]
        dest_c = c + dc[i]
        if jido[dest_r][dest_c] == 0:
            leggo = True
            jido[r][c] = 1
            r, c = dest_r, dest_c
            answer += 1
            break
    d = i % 4

print(answer)