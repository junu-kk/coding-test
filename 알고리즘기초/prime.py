# 소수 하나만 찾을때
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# arr에 있는 소수 모두 판별하고 싶을때
def is_prime_erathos(arr):
    max_n = max(arr)
    prime_t = [True] * (max_n + 1)
    prime_t[1] = False
    for i in range(2, max_n + 1):
        if prime_t[i]:
            tmp = i * 2
            while tmp <= max_n:
                prime_t[tmp] = False
                tmp += i
    answer = [prime_t[x] for x in arr]
    return answer


print(is_prime(2))
print(is_prime_erathos([3,2,123]))
