def solution(money):
    n = len(money)
    first_safe_dp_t = [0] * n # 첫 집 안턴경우
    first_unsafe_dp_t = [0] * n # 첫 집 턴경우
    
    first_safe_dp_t[1] = money[1]
    first_unsafe_dp_t[0] = money[0]
    first_unsafe_dp_t[1] = max(money[1], money[0])
    
    # 안턴경우
    for i in range(2, n):
        first_safe_dp_t[i] = max(first_safe_dp_t[i-2] + money[i], first_safe_dp_t[i-1])

    # 턴경우
    for i in range(2, n-1):
        first_unsafe_dp_t[i] = max(first_unsafe_dp_t[i-2] + money[i], first_unsafe_dp_t[i-1])

    return max(first_safe_dp_t[n-1], first_unsafe_dp_t[n-2])
    

print(solution([1,2,3,1]))