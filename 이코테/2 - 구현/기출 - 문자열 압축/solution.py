def solution(s):
    s_l = len(s)
    answer = s_l
    for cut_l in range(1, s_l//2+1):  # 1부터 절반까지 반복
        tmp_l = 0
        tmp_s = ''
        iterate_n, remainder_l = divmod(s_l, cut_l)
        banbok_count = 0  # 정확히 말하면 (실제반복횟수-1)임.

        for i in range(iterate_n):
            cut_s = s[i*cut_l:(i+1)*cut_l]
            if tmp_s == cut_s:  # 반복이 일어나는 경우
                banbok_count += 1

            else:  # 반복이 일어나지 않는 경우
                if banbok_count > 0:  # 반복이 일어났다가 이번에 깨진 경우
                    tmp_l += len(str(banbok_count+1))  # 1을 꼭 더해주자.
                tmp_l += cut_l
                tmp_s = cut_s
                banbok_count = 0
        if banbok_count > 0:  # 마지막 반복 처리
            tmp_l += len(str(banbok_count+1))
        tmp_l += remainder_l
        answer = min(tmp_l, answer)
    return answer


print(solution('a'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
