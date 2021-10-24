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

        # 중복순열은 초기화 그런거 없다.
        s.pop()


subsol(0)
