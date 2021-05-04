from collections import deque
from sys import stdin
input = stdin.readline

vn, en = map(int, input().split())
graph = [[] for _ in range(vn+1)]
indegree_t = [0]*(vn+1)  # 처음에 0으로 초기화


for _ in range(en):
    v_from, v_to = map(int, input().split())
    graph[v_from].append(v_to)
    indegree_t[v_to] += 1  # 각각의 e를 인풋받으면서 v_to의 indegree 하나씩 올려줌

q = deque([])
for v in range(1, vn+1):
    if indegree_t[v] == 0:  # 꼴찌각 큐들 싹 다 큐에 넣음
        q.append(v)

while q:
    v = q.popleft()  # 하나 뽑고
    print(v, end=' ')
    for adj_v in graph[v]:  # 고게 향하는 방향에 대해서
        indegree_t[adj_v] -= 1  # 엣지 없애고
        if indegree_t[adj_v] == 0:  # 디 앖어지면 어펜드
            q.append(adj_v)
