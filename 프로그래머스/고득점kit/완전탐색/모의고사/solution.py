def solution(answers: list):
    n = len(answers)
    counts = [0,0,0]

    # 1
    for i in range(n):
        if i % 5 == 0 and answers[i] == 1:
            counts[0] += 1
        elif i % 5 == 1 and answers[i] == 2:
            counts[0] += 1
        elif i % 5 == 2 and answers[i] == 3:
            counts[0] += 1
        elif i % 5 == 3 and answers[i] == 4:
            counts[0] += 1
        elif i % 5 == 4 and answers[i] == 5:
            counts[0] += 1

    # 2
    for i in range(n):
        if i % 2 == 0 and answers[i] == 2:
            counts[1] += 1
        elif i % 8 == 1 and answers[i] == 1:
            counts[1] += 1
        elif i % 8 == 3 and answers[i] == 3:
            counts[1] += 1
        elif i % 8 == 5 and answers[i] == 4:
            counts[1] += 1
        elif i % 8 == 7 and answers[i] == 5:
            counts[1] += 1

    # 3
    for i in range(n):
        if i % 10 in (0, 1) and answers[i] == 3:
            counts[2] += 1
        elif i % 10 in (2, 3) and answers[i] == 1:
            counts[2] += 1
        elif i % 10 in (4, 5) and answers[i] == 2:
            counts[2] += 1
        elif i % 10 in (6, 7) and answers[i] == 4:
            counts[2] += 1
        elif i % 10 in (8, 9) and answers[i] == 5:
            counts[2] += 1

    max_score = max(counts)
    answer = []
    for i in range(3):
        if counts[i] == max_score:
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))
