a, b, c = map(int, input().split())

def subsolution(a, b, c):
    if b == 1:
        return a%c
    else:
        tmp = subsolution(a, b//2, c)
        if b % 2 == 0: # 짝수면
            return tmp * tmp % c
        elif b % 2 == 1: # 홀수면
            return tmp * tmp * a % c

print(subsolution(a, b, c))
