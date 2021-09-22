# 종이에 그려가며 하면 풀만함.
tc_n = int(input())
for _ in range(tc_n):
    xn, yn = map(int, input().split())
    xs = sorted(list(map(int, input().split())))
    ys = sorted(list(map(int, input().split())))
    answer = 0
    xi, yi = 0, 0
    while xi < xn and yi < yn:
        # xi마다 비교하며 answer 올려주고
        x, y = xs[xi], ys[yi]
        if x > y:  # yi 늘리기
            yi += 1
        else:  # 정산
            answer += yi
            xi += 1
    # 막타
    if yi == yn:
        answer += (xn-xi) * yn
    print(answer)
