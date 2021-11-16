s = []
visit_t = [False] * 123


def perm(n, m, depth):
    if depth == m:
        print(s, end=' ')
        return

    for i in range(1, n + 1):
        if visit_t[i]:
            continue

        # 치고
        visit_t[i] = True
        s.append(i)

        # 재귀하고
        perm(n, m, depth + 1)

        # 빠지는
        visit_t[i] = False
        s.pop()


def comb(n, m, depth):
    if depth == m:
        print(s, end=' ')
        return

    for i in range(1, n + 1):
        if visit_t[i]:
            continue

        # 치고
        visit_t[i] = True
        s.append(i)

        # 재귀하고
        comb(n, m, depth + 1)

        # 빠지는
        for j in range(i + 1, n + 1):
            visit_t[j] = False
        s.pop()


def jungbok_perm(n, m, depth):
    if depth == m:
        print(s, end=' ')
        return

    for i in range(1, n + 1):
        # 치고
        s.append(i)

        # 재귀하고
        jungbok_perm(n, m, depth + 1)

        # 빠지고
        s.pop()


def jungbok_comb(n, m, depth):
    if depth == m:
        print(s, end=' ')
        return

    for i in range(1, n + 1):
        if visit_t[i]:
            continue

        # 치고
        s.append(i)

        # 재귀하고
        jungbok_comb(n, m, depth + 1)
        visit_t[i] = True

        # 빠지는
        for j in range(i + 1, n + 1):
            visit_t[j] = False
        s.pop()


def init():
    print()
    s.clear()
    for i in range(len(visit_t)):
        visit_t[i] = False


perm(4, 2, 0)
init()

comb(4, 2, 0)
init()

jungbok_perm(4, 2, 0)
init()

jungbok_comb(4, 2, 0)
init()
