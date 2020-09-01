# Q : 팩토리얼 함수를 반복적으로 / 재귀적으로 구현하시오.
def factorial_iterative(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer

def factorial_recursive(n):
    # 종료조건
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(10), factorial_recursive(10))