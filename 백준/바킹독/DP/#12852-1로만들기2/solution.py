'''
아까는 탑다운으로 했으니
이번엔 바텀업으로 해봄.

'''
n = int(input())
dp_t = [0] * (n + 1)
pre_t = [0] * (n + 1)
dp_t[1] = 0
for i in range(2, n+1):
    dp_t[i] = dp_t[i-1] + 1
    pre_t[i] = i-1

    if i%2 == 0 and dp_t[i] > dp_t[i//2] + 1:
        dp_t[i] = dp_t[i//2] + 1
        pre_t[i] = i//2
    if i%3 == 0 and dp_t[i] > dp_t[i//3] + 1:
        dp_t[i] = dp_t[i//3] + 1
        pre_t[i] = i//3

print(dp_t[n])
cur = n
while cur != 1:
    print(cur, end=' ')
    cur = pre_t[cur]
print(1)

