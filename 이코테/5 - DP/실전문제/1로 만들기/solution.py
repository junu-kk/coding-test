from sys import stdin
input = stdin.readline

n = int(input())
dp_t = [0]*(n+1)
for i in range(2, n+1):
    v = dp_t[i-1]+1  # 기본적으로는 전 거에서 1을 더하되
    # 만약 2나 3이나 5로 나누어 떨어진다면, 고것들도 한 번 고려해주기.
    if i % 2 == 0:
        v = min(v, dp_t[i//2]+1)
    if i % 3 == 0:
        v = min(v, dp_t[i//3]+1)
    if i % 5 == 0:
        v = min(v, dp_t[i//5]+1)

    dp_t[i] = v

print(dp_t[n])
