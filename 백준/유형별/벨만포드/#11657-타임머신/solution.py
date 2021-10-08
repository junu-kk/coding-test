'''
# io
3 4 # vn, en
1 2 4 # from, to, cost
1 3 3
2 3 -1
3 1 -2

4 # 1 -> 2
3 # 1 -> 3

# notes
cost 0 : 순간이동
cost <0 : 시간역

시간을 무한히 오래 전으로 되돌릴 수 있다면 -1

# strategy
1에서 출발하는 다익스트라로 푸는 게 정석이지만
cost가 음수일 수 있다.

# pseudo code



'''
from sys import maxsize

vn, en = map(int, input().split())
es = []
for _ in range(en):
    st, end, cost = map(int, input().split())
    es.append((st, end, cost)) # graph, mtrx 대신 es!

dist_t = [maxsize] * (vn + 1)


def belmanford(v_start):
    dist_t[v_start] = 0
    for round in range(vn-1):  # vn-1만큼 라운드를 반복함
        for st, end, cost in es:  # 각 e에 대해
            if dist_t[st] != maxsize and dist_t[end] > dist_t[st] + cost:  # dist_t[end]를 갱신할만하면 갱신
                dist_t[end] = dist_t[st] + cost

    # last round에도 갱신된다면, 그건 음수간선순환이 발생한다는 의미.
    for st, end, cost in es:
        if dist_t[st] != maxsize and dist_t[end] > dist_t[st] + cost:
            return True

    return False


negative_cycle = belmanford(1)

if negative_cycle:  # 음수 간선 순환
    print(-1)
    exit()

for v in range(2, vn + 1):
    print(-1 if dist_t[v] == maxsize else dist_t[v])
