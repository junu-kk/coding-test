# 1을 빼거나, k로 나누거나. 1이 될 때까지.
answer = 0
n, k = map(int, input().split())

while True:
    answer += 1
    if n % k == 0:
        n /= k
    else:
        n -= 1
    
    if n == 1:
        print(answer)
        break