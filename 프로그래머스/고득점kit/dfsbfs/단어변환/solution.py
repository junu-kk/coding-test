def solution(begin:str, target:str, words:list):
    answer = 0

    word_n = len(words)

    if target not in words:
        return 0

    # dfs를 돌릴건데
    visit_t = [False] * len(words)

    s = [begin]
    while s:
        word = s.pop()

        # 찾으면 리턴하고
        if word == target:
            return answer

        # 워드후보 개수만큼 반복문을 돌리는데
        for i in range(word_n):
            # 하나의 알파벳만 다르면서 처리하지 않았다면
            if one_alph_diff(words[i], word) and not visit_t[i]:
                # 처리 후 스택에 추가
                visit_t[i] = True
                s.append(words[i])

        # 뎁쓰 올리는걸 여기서 하는거구나..
        answer += 1


    
    return answer

def one_alph_diff(w1, w2):
    diff_count = 0
    for alph1, alph2 in zip(w1, w2):
        if alph1 != alph2:
            diff_count += 1

    return True if diff_count == 1 else False

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))