# 답 참조함.
from pprint import pprint

def solution(vn, es):
    # mtrx[r][c] = r이 c를 이겼는가?
    mtrx = [[None] * (vn + 1) for _ in range(vn + 1)]

    for win, lose in es:
        mtrx[win][lose] = True
        mtrx[lose][win] = False

    for v2 in range(vn + 1):
        for v1 in range(vn + 1):
            for v3 in range(vn + 1):
                # 승부차이가 없다면 컨틴뉴
                if mtrx[v1][v2] == None:
                    continue

                # v1이 V2를 이기고, v2가 V3을 이기는 경우 : V1과 V3에게 삼단논법 적용
                if mtrx[v1][v2] == mtrx[v2][v3]:
                    result = mtrx[v1][v2]
                    mtrx[v1][v3] = result
                    mtrx[v3][v1] = not result

    pprint(mtrx)
    answer = 0
    # 결국 각각에 대해 None이 아닌 걸 확인해야 함.
    for v in range(1, vn + 1):
        if None in mtrx[v][1:v] + mtrx[v][v+1:]:
            continue
        answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))