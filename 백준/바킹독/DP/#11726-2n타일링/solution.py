'''
# io
2

2 # 가로로 두개 or 세로로 두개


# notes


# strategy
비슷한 문제를 이코테에서 본 것 같다.
dp_t[1] = 1
dp_t[2] = 2
dp_t[3] = 전전거에서 가로 두개를 붙이거나, 전거에서 세로 하나를 붙이거나.



# pseudo code



'''
n = int(input())
if n in (1,2):
    print(n)
    exit()
dp_t = [0] * (n+1)
dp_t[1] = 1
dp_t[2] = 2

for i in range(3, n+1):
    dp_t[i] = (dp_t[i-2] + dp_t[i-1]) % 10007

print(dp_t[n] % 10007)