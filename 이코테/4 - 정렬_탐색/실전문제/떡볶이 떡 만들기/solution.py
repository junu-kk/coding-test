from sys import stdin
input = stdin.readline

ddeok_n, target = map(int, input().split())
ddeoks = sorted(list(map(int, input().split())))


def get_ddeok_l(cut_l):
    ddeok_l = 0
    for ddeok in ddeoks:
        l = ddeok - cut_l
        if l > 0:
            ddeok_l += l
    return ddeok_l


def binary_search(ll, rl):
    while ll <= rl:
        mid_l = (ll+rl)//2
        ddeok_l = get_ddeok_l(mid_l)
        if ddeok_l == target:
            return mid_l
        elif ddeok_l > target:
            ll = mid_l + 1
        else:
            rl = mid_l - 1

    return mid_l


print(binary_search(0, ddeoks[-1]))
