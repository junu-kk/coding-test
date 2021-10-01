n = int(input())
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:  # 나눌수있는만큼 잽싸게 나눠준다.
        print(i)
        n /= i

if n != 1:  # 작업을 마치고 남은 값이 1이 아니라면, 가장 큰 소수일 것이다.
    print(int(n))
