'''
<io>
8 # n

92 # n*n 판에서 퀸 n개를 서로 공격할 수 없게 놓는 경우의 수

<notes>


<strategy>
백트래킹 문제.
재귀로 타고타고 들어가서 n번까지 무사히 놓았을 때 종료시키면 되겠다.
이 또한 대충 스켈레톤만 짜놓고, 실제 정답코드 보면서 비교해보자.
각 row마다 하나씩 놓는 방향으로 간다면, r이 곧 depth임.
s = []
subsol(r):
    if r == n:
        answer += 1
        return

    for c in range(n):
        if available(r, c):
            s.append((r,c))
            subsol(depth+1)
            s.pop()


'''
n = int(input())
mtrx = [[True] * n for _ in range(n)]
answer = 0

def available(r, c):
    row = mtrx[r]
    for tmp_c in range(c):
        if row[c] == row[tmp_c] or abs(row[c] - row[tmp_c]) == c-tmp_c:
            return False
    return True

def subsol(r):
    global answer, n

    if r == n:
        answer += 1
        return

    for c in range(n):
        mtrx[r][c] = False
        if available(r, c):
            subsol(r+1)
        mtrx[r][c] = True

subsol(0)
print(answer)