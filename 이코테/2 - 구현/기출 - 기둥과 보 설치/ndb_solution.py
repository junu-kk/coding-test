GIDUNG = DELETE = 0
BO = CREATE = 1


def possible(answer):
    for x, y, gb in answer:
        if gb == GIDUNG:
            # 기둥이 존재할 조건 3개 중 하나에 해당하면 정상
            if not (y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer):
                return False
        elif gb == BO:
            # 보가 존재할 조건 2개 중 하나에 해당하면 정상
            if not ([x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer)):
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, gb, cd = frame
        if cd == CREATE:
            answer.append([x, y, gb])
            if not possible(answer):
                answer.pop()
        elif cd == DELETE:
            answer.remove([x, y, gb])
            if not possible(answer):
                answer.append([x, y, gb])

    return sorted(answer)


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
