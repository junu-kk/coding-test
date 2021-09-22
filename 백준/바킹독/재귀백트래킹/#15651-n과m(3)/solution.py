n, m = map(int, input().split())
s = []

# 중복순열
def subsol(depth):
    global n, m
    if depth == m:
        print(' '.join(map(str, s)))
        return

    # n중반복문의 기본 == 재귀
    for i in range(n):
        num = i+1
        # 치고
        s.append(num)

        # 재귀하고
        subsol(depth + 1)

        # 빠지고 -> perm에선 i를 초기화시켜준 반면, comb에선 i+1부터 끝까지를 초기화시켜주고 있다!
        s.pop()


subsol(0)
