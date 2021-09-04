def get_brown_n(y_garo, y_sero):
    return y_garo*2 + y_sero*2 + 4


def solution(brown:int, yellow:int):
    for y_sero in range(1, int(yellow**0.5)+1):
        if yellow % y_sero == 0:
            y_garo = yellow//y_sero
            if get_brown_n(y_garo, y_sero) == brown:
                return [y_garo+2, y_sero+2]


    return 0


print(solution(10, 2))