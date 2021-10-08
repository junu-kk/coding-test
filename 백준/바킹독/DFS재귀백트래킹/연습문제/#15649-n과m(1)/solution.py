n, m = map(int, input().split())
visit_t = [False] * n # 인엑스 i 는 숫자 i+1를 뜻함.
s = []

# 순열
def subsol(depth):
    global n, m

    if depth == m:
        print(*s)
        return

    for i in range(n):
        if visit_t[i]:
            continue

        num = i+1
        # 치고
        visit_t[i] = True
        s.append(num)

        # 재귀하고
        subsol(depth + 1)

        # 빠지고 -> perm에선 i를 초기화시켜준 반면, comb에선 i+1부터 끝까지를 초기화시켜주고 있다!
        visit_t[i] = False
        s.pop()


subsol(0)
