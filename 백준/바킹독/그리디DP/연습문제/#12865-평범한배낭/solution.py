'''
# io
4 7 # 물건 4개, 맥스무게 7
6 13 # 무게와 가치
4 8
3 6
5 12


# notes


# strategy
dp_t를 2차원으로 해야 한다.
dp_t[n][k] : n번째 물건까지 살펴봤을 때, 무게가 k인 배낭의 최대 가치


# pseudo code
허용무게 < 넣을무게:
    break
max(직전가치, 이전가치 + 현가치)


'''
obj_n, max_w = map(int, input().split())
objs = [[0, 0]]
for _ in range(obj_n):
    objs.append(tuple(map(int, input().split())))  # w, v

dp_t = [[0] * (max_w + 1) for _ in range(obj_n + 1)]
for obj_i in range(1, obj_n + 1):
    for tmp_max_w in range(1, max_w + 1):
        w, v = objs[obj_i]
        if tmp_max_w < w:  # w를 뺄 건덕지도 없다면
            dp_t[obj_i][tmp_max_w] = dp_t[obj_i - 1][tmp_max_w]
        else:
            dp_t[obj_i][tmp_max_w] = max(dp_t[obj_i - 1][tmp_max_w], dp_t[obj_i - 1][tmp_max_w - w] + v)

print(dp_t[obj_i][max_w])
