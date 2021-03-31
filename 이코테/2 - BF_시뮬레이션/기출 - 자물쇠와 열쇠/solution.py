'''
000    010
100 -> 100
011    100

00 02
01 12
02 22
10 01
11 11
12 21
...
'''
BOLT = 1
NUT = 0
OK = 2


def rotate_clockwise(n, mtrx):
    new_mtrx = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_mtrx[r][c] = mtrx[c][n - r - 1]
    return new_mtrx


def solution(key, lock):
    key_l = len(key)
    lock_l = len(lock)
    jido_l = lock_l+key_l*2-2  # 지도는 키가 귀퉁이에 끼어도 딱 차도록 설정.
    jido = [[OK]*(jido_l) for _ in range(jido_l)]
    for r in range(lock_l):
        for c in range(lock_l):
            jido[r+key_l-1][c+key_l-1] = lock[r][c]

    def fit(key, jido, start_r, start_c):
        for r in range(key_l):
            for c in range(key_l):
                if not (jido[start_r+r][start_c+c] == OK or (jido[start_r+r][start_c+c] == BOLT and key[r][c] == NUT) or (jido[start_r+r][start_c+c] == NUT and key[r][c] == BOLT)):
                    return False
        return True

    for _ in range(4):
        key = rotate_clockwise(key_l, key)
        for r in range(key_l+lock_l-1):
            for c in range(key_l+lock_l-1):
                if fit(key, jido, r, c):
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
