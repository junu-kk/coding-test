'''
# io
3
10 12 3 9 # 10 12에서 <3:9>는?
10 12 7 2
13 11 5 6

33
-1 # 유효하지 않은 표현인 경우
83

# notes
10 12일때
<1:1> : 이 세상의 시초
<2:2> : 그 다음
...
10 10
1 11
2 12
3 1
그냥 iterate인듯?

# strategy
x%n == y%n


'''

n = int(input())
for _ in range(n):
    x_max, y_max, x, y = map(int, input().split())
    in_range = False
    while x <= x_max * y_max:
        if x % y_max == y % y_max:
            in_range = True
            break
        x += x_max # x는 계속해서 x_max만큼 올려준다.
    print(x if in_range else -1)
