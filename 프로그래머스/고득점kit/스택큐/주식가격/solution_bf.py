def solution(prices: list):
    n = len(prices)
    answer = []
    for i in range(n):
        gijun = prices[i]
        stable_count = 0
        for price in prices[i + 1:]:
            stable_count += 1
            if gijun > price:
                break

        answer.append(stable_count)

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2]))
print(solution([2, 1]))
