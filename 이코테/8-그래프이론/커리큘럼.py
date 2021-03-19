from collections import deque
from copy import deepcopy

vn = int(input())
indegree = [0] * (vn + 1)
graph = [[] for i in range(vn + 1)]
time = [0] * (vn+1)

for i in range(1, vn+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = deepcopy(time)
    q = deque()

    for i in range(1, vn+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, vn+1):
        print(result[i])

topology_sort()