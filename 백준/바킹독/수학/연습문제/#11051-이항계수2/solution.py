n, k = map(int, input().split())

bunja = 1
bunmo = 1

for i in range(min(n-k, k)):
    bunja = bunja * (n - i)
    bunmo = bunmo * (i + 1)

print((bunja // bunmo) % 10007)
