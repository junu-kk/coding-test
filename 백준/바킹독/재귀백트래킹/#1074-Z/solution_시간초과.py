'''
<io>
2 3 1 # 2^2 x 2^2 mtrx에서 [3][1]에 있는 숫자는?

11

<notes>
라인 코테에서 이와 비슷한 문제가 나왔다. 한 번 혼자 힘으로 해결해보자.

<strategy>
일단 초기화를 해주자.
real_n = 1<<n
mtrx = [[-1] * real_n for _ in range(real_n)]

이문제.. 할만했네
다만 메모리 초과가 나는 것을 해결해야 할 것이다.


'''

n, r, c = map(int, input().split())
real_n = 1 << n
mtrx = [[-1] * real_n for _ in range(real_n)]
x = 0


def subsol(n, r, c, x):
    if n == 1:
        mtrx[r][c] = x
        mtrx[r][c+1] = x+1
        mtrx[r+1][c] = x+2
        mtrx[r+1][c+1] = x+3
        return

    danwi = 1 << n - 1
    danwi2 = 1 << danwi
    subsol(n - 1, r, c, x)
    subsol(n - 1, r, c + danwi, x + danwi2)
    subsol(n - 1, r + danwi, c, x + 2*danwi2)
    subsol(n - 1, r + danwi, c + danwi, x + 3*danwi2)


subsol(n, 0, 0, 0)
print(mtrx[r][c])
