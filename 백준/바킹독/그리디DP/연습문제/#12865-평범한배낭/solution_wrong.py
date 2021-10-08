'''
# io
4 7 # 물건 4개, 맥스무게 7
6 13 # 무게와 가치
4 8
3 6
5 12


# notes


# strategy
그리디로 한다면, 가성비대로 넣겠지만
결국 dp로 풀어야 할 것 같다.

다만 이걸 넣었었는지, 안넣었었는지 기록해야 할텐데


# pseudo code



'''
obj_n, max_w = map(int, input().split())
objs = []
for _ in range(obj_n):
    objs.append(tuple(map(int, input().split())))  # w, v

objs.sort()
dp_t = [0] * (max_w + 1)  # 인덱스는 최대무게, 값은 최대가치합
set_t = [set()] * (max_w + 1)
for tmp_max_w in range(1, max_w + 1):
    # print(f'{tmp_max_w} 차례')
    change = False
    for i in range(obj_n):
        w, v = objs[i]
        if tmp_max_w < w:
            break
        if i in set_t[tmp_max_w - w]:
            continue
        if dp_t[tmp_max_w - 1] < dp_t[tmp_max_w - w] + v:
            dp_t[tmp_max_w] = dp_t[tmp_max_w - w] + v
            set_t[tmp_max_w] = set_t[tmp_max_w - w] | {i}
            change = True

    if not change:
        dp_t[tmp_max_w] = dp_t[tmp_max_w - 1]
        set_t[tmp_max_w] = set_t[tmp_max_w - 1]

# print(dp_t)
# print(set_t)
print(dp_t[max_w])
