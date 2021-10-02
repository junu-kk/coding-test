'''
# io
2

1 # 1로 만드는데 1회면 충분하다.


# notes
3으로 나누거나
2로 나누거나
1을 빼거나

# strategy
dp_t n+1 크기로 만든담에 싹 다 INF로 초기화해주고
쭉 내려오면서 min(dp_t[i+1], dp_t[2i], dp_t[3i]) + 1 해주면 되겠다.

bfs로도 할 순 있겠다.

# pseudo code



'''
from sys import maxsize
n = int(input())
dp_t = [maxsize] * (3*n+1)
dp_t[n] = 0
for i in range(n-1, 0, -1):
    dp_t[i] = min(dp_t[i+1], dp_t[i*2], dp_t[i*3]) + 1

# print(dp_t)
print(dp_t[1])