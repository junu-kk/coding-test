# ~48

N = int(input())
g_s = []
for i in range(N):
    g_s.append(tuple(input().split()))

for each in sorted(g_s, key=lambda x: x[1]):
    print(each[0], end=' ')
