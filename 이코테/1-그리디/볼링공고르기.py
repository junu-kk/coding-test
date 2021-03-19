n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls_dict={}
answer = int(n * (n-1) / 2)
# 중복검사 해야되는데.. 딕셔너리에 넣을까?
for ball in balls:
    if ball not in balls_dict:
        balls_dict[ball] = 1
    else:
        balls_dict[ball] += 1

for each in balls_dict.items():
    if each[1] >= 2:
        answer -= int((each[1] * (each[1]-1) / 2))

print(answer)