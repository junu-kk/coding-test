def solution(n, build_frame):
    BLANK = -1
    GIDUNG = DELETE = 0
    BO = CREATE = 1
    GIBO = 2

    jido = [[BLANK]*(n+1) for _ in range(n+1)]

    def is_in_map(x, y):
        if 0 <= x <= n and 0 <= y <= n:
            return True
        return False

    def gidung_create_available(x, y):
        if y == 0:
            return True

        if is_in_map(x-1, y) and jido[x-1][y] == BO:
            return True

        if is_in_map(x, y-1) and jido[x][y-1] == GIDUNG:
            return True

        return False

    def bo_create_available(x, y):
        if is_in_map(x, y-1) and jido[x][y-1] == GIDUNG:
            return True

        if is_in_map(x+1, y-1) and jido[x+1][y-1] == GIDUNG:
            return True

        if is_in_map(x-1, y) and is_in_map(x+1, y) and jido[x-1][y] == BO and jido[x+1][y] == BO:
            return True

        return False

    def delete_gidung(x, y):
        jido[x][y] = BLANK
        if is_in_map(x, y+1) and jido[x][y+1] == BO:
            if not bo_create_available(x, y+1):
                jido[x][y] = GIDUNG
                return
        if is_in_map(x, y+1) and jido[x][y+1] == GIDUNG:
            if not gidung_create_available(x, y+1):
                jido[x][y] = GIDUNG
                return
        if is_in_map(x-1, y+1) and jido[x-1][y+1] == BO:
            if not bo_create_available(x-1, y+1):
                jido[x][y] = GIDUNG
                return

    def delete_bo(x, y):
        jido[x][y] = BLANK
        if is_in_map(x+1, y) and jido[x+1][y] == GIDUNG:
            if not gidung_create_available(x+1, y):
                jido[x][y] = BO
                return
        if is_in_map(x+1, y) and is_in_map(x-1, y) and jido[x+1][y] == BO and jido[x-1][y] == BO:
            if not (bo_create_available(x+1, y) and bo_create_available(x-1, y)):
                jido[x][y] = BO
                return

    for frame in build_frame:
        x, y, gb, cd = frame
        if cd == CREATE:
            if gb == GIDUNG and gidung_create_available(x, y):
                jido[x][y] = GIDUNG
            elif gb == BO and bo_create_available(x, y):
                jido[x][y] = BO
        elif cd == DELETE:
            if gb == GIDUNG:
                delete_gidung(x, y)
            elif gb == BO:
                delete_bo(x, y)

    answer = []
    for x in range(n+1):
        for y in range(n+1):
            if jido[x][y] == GIDUNG:
                answer.append([x, y, GIDUNG])
            elif jido[x][y] == BO:
                answer.append([x, y, BO])

    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
