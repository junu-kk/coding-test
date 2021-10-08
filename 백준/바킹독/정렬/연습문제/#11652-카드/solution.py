'''
# io
5
1
2
1
2
1

1

# notes


# strategy


# pseudo code



'''
from collections import defaultdict as dd
n = int(input())

d = dd(int)
for _ in range(n):
    d[int(input())] += 1
print(max(d.items(), key=lambda x:(x[1], -x[0]))[0])