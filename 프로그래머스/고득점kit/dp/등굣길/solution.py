from pprint import pprint

INF = int(1e9)


def solution(cn: int, rn: int, puddles: list) -> int:
    dp_t = [[0] * (cn + 1) for _ in range(rn + 1)]
    for r in range(rn + 1):
        dp_t[r][0] = INF
    for c in range(cn + 1):
        dp_t[0][c] = INF
    for pc, pr in puddles:
        dp_t[pr][pc] = INF

    dp_t[1][1] = 1

    for r in range(1, rn + 1):
        for c in range(1, cn + 1):
            if dp_t[r][c] == INF:
                continue

            if dp_t[r - 1][c] != INF and dp_t[r][c - 1] != INF:
                dp_t[r][c] = dp_t[r - 1][c] + dp_t[r][c - 1]
            elif dp_t[r - 1][c] == INF and dp_t[r][c-1] != INF:
                dp_t[r][c] = dp_t[r][c - 1]
            elif dp_t[r - 1][c] != INF and dp_t[r][c - 1] == INF:
                dp_t[r][c] = dp_t[r - 1][c]
            else: # INF INF 인 경우 INF
                pass

    return dp_t[rn][cn]%1000000007


print(solution(4, 3, [[2, 2]]))
