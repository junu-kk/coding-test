'''
비트마스크에 대한 이해가 선행되어야 할 것 같다.

<io>
vn
v_start
v_end
es
trap_vs

result

<notes>
함정을 밟으면: 트랩과 연결된 화살표 방향이 바뀜 (io 모두)
방향 가중치 그래프

<strategy>
트랩이 없었다면..
그냥 1번에서 출발하는 걸로 다익스트라 쓰면 됨. (다익 복습해야겠다.)

<사전지식>
and &
or |
xor ^
shift << >>
not ~

'''

from heapq import heappush, heappop


def solution(vn, v_start, v_end, es, trap_vs):
    INF = int(1e9)
    NON_TRAP = -1

    # 원래 dist_t는 INF가 vn+1 있는건데, 거기에 각 상태까지 해서 1024 뻥튀기.
    # 즉 원래같으면 [v]에 dist가 저장되어 있겠지만
    # 여기선 [v][status]에 dist가 저장되어있음.
    dist_2d_t = [[INF] * 1024 for _ in range(vn + 1)]

    # 정방향 / 역방향 간선
    std_es = [[] for _ in range(vn + 1)]
    rev_es = [[] for _ in range(vn + 1)]

    trap_t = [NON_TRAP] * (vn + 1)  # 노드 v의 함정번호는 trap_t[v]. 기본값은 NON_TRAP

    for from_v, to_v, cost in es:
        std_es[from_v].append((to_v, cost))
        rev_es[to_v].append((from_v, cost))

    # 트랩에 각자 다른 번호를 0부터 매겨줌
    for i in range(len(trap_vs)):
        trap_v = trap_vs[i]
        trap_t[trap_v] = i

    dist_2d_t[v_start][0] = 0
    h = [(dist_2d_t[v_start][0], v_start, 0)]  # 0은 상태를 뜻함.

    # status에 i번 비트가 켜져있는가?
    def bitmask(status, i):
        return (1 << trap_t[i]) & status

    while h:
        dist, v, status = heappop(h)

        # 이렇게 끝내도 되는건가?
        if v == v_end:
            return dist

        if dist_2d_t[v][status] != dist:
            continue

        for adj_v, adj_dist in std_es[v]: # 인접한 엣지에 대하여
            rev = False
            if trap_t[v] != NON_TRAP and bitmask(status, v):
                rev = not rev
            if trap_t[adj_v] != NON_TRAP and bitmask(status, adj_v):
                rev = not rev
            if rev:
                continue

            next_status = status
            if trap_t[adj_v] != NON_TRAP:
                next_status ^= (1 << trap_t[adj_v])

            dist_new = dist + adj_dist
            if dist_new < dist_2d_t[adj_v][next_status]:
                dist_2d_t[adj_v][next_status] = dist_new
                heappush(h, (dist_2d_t[adj_v][next_status], adj_v, next_status))

        for adj_v, adj_dist in rev_es[v]:
            rev = False
            if trap_t[v] != NON_TRAP and bitmask(status, v):
                rev = not rev
            if trap_t[adj_v] != NON_TRAP and bitmask(status, adj_v):
                rev = not rev
            if not rev:
                continue

            next_status = status
            if trap_t[adj_v] != NON_TRAP:
                next_status ^= (1 << trap_t[adj_v])

            dist_new = dist + adj_dist
            if dist_new < dist_2d_t[adj_v][next_status]:
                dist_2d_t[adj_v][next_status] = dist_new
                heappush(h, (dist_2d_t[adj_v][next_status], adj_v, next_status))

    # 탈출 못한다면 (문제조건은 항상 탈출 가능한상황만 주어짐)
    return -1


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
