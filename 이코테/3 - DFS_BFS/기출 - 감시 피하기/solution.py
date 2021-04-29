def solution():
    from itertools import combinations

    BLANK = 'X'
    STUDENT = 'S'
    TEACHER = 'T'
    OBSTACLE = 'O'

    n = int(input())
    jido = []
    blanks = []
    teachers = []
    for r in range(n):
        row = input().split()
        for c in range(n):
            if row[c] == BLANK:
                blanks.append((r, c))
            elif row[c] == TEACHER:
                teachers.append((r, c))
        jido.append(row)

    answer = 0

    for comb_obstacles in combinations(blanks, 3):
        for obstacle in comb_obstacles:
            r, c = obstacle
            jido[r][c] = OBSTACLE

        avoidable = True
        for teacher in teachers:
            teacher_r, teacher_c = teacher
            for r in range(teacher_r-1, -1, -1):  # 선생 위 ~ 위끝
                if jido[r][teacher_c] == OBSTACLE:
                    break
                if jido[r][teacher_c] == STUDENT:
                    avoidable = False
                    break
            for r in range(teacher_r+1, n):  # 선생 아래 ~ 아래끝
                if jido[r][teacher_c] == OBSTACLE:
                    break
                if jido[r][teacher_c] == STUDENT:
                    avoidable = False
                    break
            for c in range(teacher_c-1, -1, -1):  # 선생 왼 ~ 왼끝
                if jido[teacher_r][c] == OBSTACLE:
                    break
                if jido[teacher_r][c] == STUDENT:
                    avoidable = False
                    break
            for c in range(teacher_c+1, n):  # 선생 오른 ~ 오른끝
                if jido[teacher_r][c] == OBSTACLE:
                    break
                if jido[teacher_r][c] == STUDENT:
                    avoidable = False
                    break

        if avoidable:
            return True

        for obstacle in comb_obstacles:
            r, c = obstacle
            jido[r][c] = BLANK

    return False


print('YES' if solution() else 'NO')
