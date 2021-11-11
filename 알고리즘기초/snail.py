'''
ref : https://somefood.github.io/algorithm/2020/07/13/algorithm_snail/
012
783
654

0123
1234
0545
9876

'''


# 정사각형일 경우
def pprint(mtrx):
    print('[')
    for row in mtrx:
        print(*row)
    print(']')


# 열증 행증 열감 행감
def generate_snail_mtrx(n):
    mtrx = [[0] * n for _ in range(n)]
    r = 0
    c = -1
    cnt = 1  # 넣을 값
    buho = 1  # 증가하는지 감소하는지

    while n > 0:
        for i in range(n):
            c += buho  # 열 옮기고
            mtrx[r][c] = cnt  # 찍고
            cnt += 1  # 다음 숫자로
        n -= 1
        for i in range(n):
            r += buho  # 행 옮기고
            mtrx[r][c] = cnt  # 찍고
            cnt += 1  # 다음 숫자로
        buho *= -1
    return mtrx
