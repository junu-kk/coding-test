# 피보나치는 쭈루룩 더하는거였지.
# 1 1 2 3 5 ...

def fibo_slow(x): # 재귀재귀재귀재귀 새로계산 새로계산 -> 시간 매우 오래 걸림.
    if x == 1 or x == 2:
        return 1
    return fibo_slow(x-1) + fibo_slow(x-2)

d1 = [0] * 100 # 메모이제이션 위한 리스트 초기화. 메모이제이션을 위한 DP테이블

def fibo_topdown(x): # 탑다운은 주로 재귀 사용
    if x == 1 or x == 2:
        return 1
    if d1[x] != 0: # 계산한 것이라면 그거 꺼내오기
        return d1[x]
    d1[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return d1[x]

def fibo_bottomup(x): # 바텀업은 주로 반복문 사용
    d2 = [0] * 100
    d2[1] = 1
    d2[2] = 1
    n = 99
    for i in range(3, x+1):
        d2[i] = d2[i-1] + d2[i-2]
    return d2[x]

print(fibo_slow(10))
print(fibo_topdown(10))
print(fibo_bottomup(10))
    