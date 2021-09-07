def solution(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성 -> 시간을!!!! 저장한다!!!!
    s = []

    for i in range(n):
        # 1. 스택 비지 않고, prices[top] > prices[i] 이라면 다음 반복
        # 1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 1-2. answer[top]에 i - top을 저장
        while s and prices[s[-1]] > prices[i]:
            top = s.pop()
            answer[top] = i - top
        # 2. 스택에 현재 시간 i 저장
        s.append(i)

    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while s:
        # 1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = s.pop()
        answer[top] = n - 1 - top

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2]))
print(solution([2, 1]))
