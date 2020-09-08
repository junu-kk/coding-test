# ~53

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(n):
    if k <= 0:
        break

    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

    k -= 1

print(sum(a))
