import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

vn = int(input())
parent_t = [0] * (vn + 1)
depth_t = [-1] * (vn + 1)  # -1이면 아직 뎁쓰계산 안한거.
graph = [[] for _ in range(vn + 1)]

'''
사실 트리를 나타내는 방법은
정석적인 클래스 구현 : 잘 안나온다.
리스트 구현 : 힙으로 많이 쓰인다.
그래프로 구현 : 이런 문제에서 활용할 수 있겠다.
'''
for _ in range(vn - 1):  # 그래프랑 같이 생각해줌.
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


# 각 노드에 대해 깊이 구하는 함수. depth는 0부터 출발해 재귀시마다 하나씩 늘어감.
# 엣지는 양방향으로 되어있지만 위에서부터 dfs해나가는 형태라서 괜찮다.
def fill_depth_t(v, depth):
    depth_t[v] = depth
    for adj_v in graph[v]:
        if depth_t[adj_v] == -1:  # 아직 깊이를 안구했다면 구해주기
            parent_t[adj_v] = v
            fill_depth_t(adj_v, depth + 1)


# v1과 v2의 최소 공통 조상을 리턴하는 함수
def lca(v1, v2):
    # 깊이를 맞춰 올라간 다음
    while depth_t[v1] != depth_t[v2]:
        if depth_t[v1] > depth_t[v2]:
            v1 = parent_t[v1]
        else:
            v2 = parent_t[v2]

    # 노드가 같아질때까지 동시에 올라감.
    while v1 != v2:
        v1 = parent_t[v1]
        v2 = parent_t[v2]
    return v1


fill_depth_t(1, 0)

n = int(input())
for _ in range(n):
    v1, v2 = map(int, input().split())
    print(lca(v1, v2))
