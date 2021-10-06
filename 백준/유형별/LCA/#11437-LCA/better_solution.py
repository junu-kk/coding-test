import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

LOG = 21

vn = int(input())
parent_t = [[0] * LOG for _ in range(vn + 1)]
depth_t = [0] * (vn + 1)
depth_counted_t = [False] * (vn + 1)
graph = [[] for _ in range(vn + 1)]

for _ in range(vn - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


# 각 노드에 대해 깊이 구하는 함수. depth는 0부터 출발해 재귀시마다 하나씩 늘어감.
def dfs(v, depth):
    depth_counted_t[v] = True
    depth_t[v] = depth
    for adj_v in graph[v]:
        if depth_counted_t[adj_v]:
            continue
        parent_t[adj_v][0] = v
        dfs(adj_v, depth + 1)


def set_parent():
    dfs(1, 0)
    for bumo in range(1, LOG):
        for v in range(1, vn + 1):
            parent_t[v][bumo] = parent_t[parent_t[v][bumo - 1]][bumo - 1]


def lca(v1, v2):
    # 깊이를 맞춰 올라간 다음
    if depth_t[v1] > depth_t[v2]:
        v1, v2 = v2, v1

    for bumo in range(LOG - 1, -1, -1):
        if depth_t[v2] - depth_t[v1] >= 1 << bumo:
            v2 = parent_t[v2][bumo]

    if v1 == v2:
        return v1

    for bumo in range(LOG - 1, -1, -1):
        if parent_t[v1][bumo] != parent_t[v2][bumo]:
            v1 = parent_t[v1][bumo]
            v2 = parent_t[v2][bumo]

    return parent_t[v1][0]


set_parent()

n = int(input())
for _ in range(n):
    v1, v2 = map(int, input().split())
    print(lca(v1, v2))
