'''
# io
3 : tc 3개
4 : 1111 211 121 112 31 13 22
7
10

7
44
274

# notes


# strategy
dp_t[n] : n을 만들기 위한 123 경우의 수
dp_t[1] : 1
dp_t[2] : 2
dp_t[3] : 4
dp_t[4]
    dp_t[1]에 3을  붙이거나
    dp_t[2]에 2를  붙이거나
    dp_t[3]에 1을  붙이거나
    즉 1 + 2 + 4



# pseudo code



'''
tc_n = int(input())
ns = [int(input()) for _ in range(tc_n)]
max_n = max(ns)
dp_t = [0] * (max_n + 1)
dp_t[1] = 1
dp_t[2] = 2
dp_t[3] = 4

for i in range(4, max_n+1):
    dp_t[i] = dp_t[i-1] + dp_t[i-2] + dp_t[i-3]

for n in ns:
    print(dp_t[n])