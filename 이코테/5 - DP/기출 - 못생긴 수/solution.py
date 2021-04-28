n = int(input())
ugly_t = [False]*(n*2+1)
ugly_t[1] = True
for i in range(2, 2*n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        ugly_t[i] = True

ugly_count = 0
for i in range(2*n+1):
    if ugly_t[i]:  # 못생겼을 경우 카운트 1 증가
        ugly_count += 1
        if ugly_count == n:
            print(i)
            break
