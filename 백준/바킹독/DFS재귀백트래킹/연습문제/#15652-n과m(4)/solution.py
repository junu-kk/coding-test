n, m = map(int, input().split())
visit_t = [False] * n  # 인엑스 i 는 숫자 i+1를 뜻함.
s = []


# 중복조합
def subsol(depth):
    global n, m
    if depth == m:
        print(' '.join(map(str, s)))
        return

    for i in range(n):
        if visit_t[i]:
            continue

        num = i + 1
        # 치고
        s.append(num)

        # 재귀하고
        subsol(depth + 1)

        # 빠지고
        visit_t[i] = True
        s.pop()

        for j in range(i + 1, n):
            visit_t[j] = False


subsol(0)
