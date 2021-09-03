def solution(N: int, number: int):
    # dp_t[x] : 숫자 x번 써서 만들 수 있는 수들의 집합
    # 0번 쓰면 아무것도 못만드니 None
    # 1번 쓰면 N밖에 못만드니 set([N])
    dp_t = [None, set([N])]

    # 한번에 될 경우 1 리턴
    if N == number:
        return 1

    # 그 다음부터의 case_set을 만들거임.
    for i in range(2, 9):
        # case_set : 숫자 i번 써서 만들 수 있는 수의 집합
        case_set = set([int(str(N) * i)])

        # 4면 1~2와 4~3으로 반복문 돌리면서 사칙연산
        for i_half in range(1, i // 2 + 1):
            for x in dp_t[i_half]:
                for y in dp_t[i - i_half]:
                    case_set.add(x + y)
                    case_set.add(abs(x-y))
                    case_set.add(x * y)
                    if x != 0:
                        case_set.add(y // x)
                    if y != 0:
                        case_set.add(x // y)

        if number in case_set:
            return i
        dp_t.append(case_set)
    return -1




print(solution(5, 12))
