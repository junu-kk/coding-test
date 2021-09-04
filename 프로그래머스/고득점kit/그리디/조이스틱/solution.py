def solution(name: str):
    changes = []
    for alph in name:
        changes.append(min(ord(alph) - ord('A'), ord('Z') - ord(alph) + 1))
    i = 0
    answer = 0

    while True:
        answer += changes[i]
        changes[i] = 0
        if sum(changes) == 0:
            return answer

        l, r = 1, 1
        # 다음 알파벳을 바꾸기 위한 최소이동거리를 찾을 후
        while changes[i - l] == 0:
            l += 1
        while changes[i + r] == 0:
            r += 1

        # 그 중 작은걸로 반영하고 인덱스 이동
        answer += l if l < r else r
        i += -l if l < r else r

    return answer


print(solution("JEROME"))
