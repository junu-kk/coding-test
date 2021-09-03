from copy import deepcopy
from pprint import pprint


def solution(triangle: list) -> int:
    n = len(triangle)
    dp_t = deepcopy(triangle)

    for r in range(1, n):
        for c in range(r+1):
            if c == 0:
                dp_t[r][c] += dp_t[r - 1][c]
            elif c == r:
                dp_t[r][c] += dp_t[r - 1][c - 1]
            else:
                dp_t[r][c] += max(dp_t[r - 1][c - 1], dp_t[r - 1][c])

    return max(dp_t[n - 1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
