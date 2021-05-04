from math import ceil
INF = int(1e9)

jip_n, gong_n = map(int, input().split())
jips = []
for _ in range(jip_n):
    jips.append(int(input()))

jips.sort()

dist = ceil((jip_n+1)//gong_n)
answer = INF
for i in range(jip_n-gong_n+1):
    answer = min(answer, jips[i+dist]-jips[i])

print(answer)
