
n, r, c = map(int, input().split())


def subsol(n, r, c):
    if n == 0:
        return 0

    half = 1 << (n-1)
    if r<half and c < half:
        return subsol(n-1, r, c)
    elif r<half and c>= half:
        return half*half + subsol(n-1, r, c-half)
    elif r >= half and c<half:
        return 2*half*half + subsol(n-1, r-half, c)
    else:
        return 3*half*half + subsol(n-1, r-half, c-half)


print(subsol(n, r, c))