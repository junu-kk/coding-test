def solution(citations:list):
    n = len(citations)
    citations.sort()
    for i in range(n-1, -1, -1):
        if citations[n-1-i] >= i+1:
            return i+1


    return 0


print(solution([3,0,6,1,5]))