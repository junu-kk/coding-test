from collections import deque
from copy import deepcopy

vn = int(input())
indegree_t = [0] * (vn + 1)  # (원래 했었던) 들어오는 간선의 개수
graph = [[] for _ in range(vn + 1)]
times = [0] * (vn+1)  # (새로 만드는) 각 과목별로 걸리는 시간

for i in range(1, vn+1):
    data = list(map(int, input().split()))
    times[i] = data[0]  # 일단 과목이 시간 얼마나 걸리는지 넣어주고
    for x in data[1:-1]:  # 이럴 땐 슬라이싱을 써도 되는구나.
        indegree_t[i] += 1  # 기존에 했던 것처럼 그래프&인디그리 반영
        graph[x].append(i)


def topology_sort():
    result = deepcopy(times)  # 과목별로 걸리는 시간. 이것보다 더 걸리도록 만들어야겠지.
    q = deque()

    for v in range(1, vn+1):  # 똑같이 차수 0인거 넣어주고
        if indegree_t[v] == 0:
            q.append(v)

    while q:
        v = q.popleft()
        for adj_v in graph[v]:
            result[i] = max(result[adj_v], result[v]+times[adj_v])  # 더 걸리도록.
            indegree_t[i] -= 1
            if indegree_t[i] == 0:
                q.append(i)

    for i in range(1, vn+1):
        print(result[i])


topology_sort()
