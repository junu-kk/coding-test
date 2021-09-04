def get_dist(alph: str):
    return min(abs(ord(alph) - ord('a')), abs(ord('a') - ord(alph) + 26))


def get_longest_a_substring(name: str):
    combo = False
    substring_idxs = []
    for i in range(len(name)):
        alph = name[i]
        if alph == 'a' and not combo:  # 콤보시작하는경우
            start_i = i
            combo = True
        elif alph != 'a' and combo:  # 콤보깨진경우
            end_i = i - 1
            combo = False
            substring_idxs.append((start_i, end_i))

    if combo:  # 막처리
        substring_idxs.append((start_i, len(name) - 1))

    max_substring_len = max(substring_idxs, key=lambda x: x[1] - x[0])[2]

    answer = len(name)
    answer_start_i = 0
    answer_end_i = len(name)-1
    for start_i, end_i in substring_idxs:
        if end_i-start_i == max_substring_len:
            # 첫번째와의 거리 비교. end_i든 start_i든.
            if answer < min(start_i, len(name)-end_i):
                answer_start_i = start_i
                answer_end_i = end_i
                answer = min(start_i, len(name)-end_i)

    if answer_start_i == 0 and answer_end_i == len(name)-1:
        return False
    else:
        return (answer_start_i, answer_end_i)

def solution(name: str):
    answer = 0
    for alph in name:
        answer += get_dist(alph)

    if get_longest_a_substring(name):
        start_i, end_i = get_longest_a_substring(name)
        answer += start_i-1



    return 0


print(solution("JEROEN"))
