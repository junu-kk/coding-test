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


'''
n = int(input())
for _ in range(n):
    xmax, ymax, target_x, target_y = map(int, input().split())
    x, y = 1, 1
    year = 1
    in_range = False
    while not (x == xmax and y == ymax):
        if x == target_x and y == target_y:
            in_range = True
            break

        x = x + 1 if x != xmax else 1
        y = y + 1 if y != ymax else 1

        year += 1

    print(year if in_range else -1)
