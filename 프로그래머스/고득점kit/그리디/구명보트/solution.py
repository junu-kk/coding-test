def solution(people: list, limit: int):
    n = len(people)
    people.sort()
    answer = 0
    i = 0
    j = n-1
    while i<=j:
        answer += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return answer


print(solution([70, 50, 80, 50], 100))
