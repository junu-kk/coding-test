'''
# io
4 vn
0 10 15 20 adj_mtrx
5 0 9 10
6 13 0 12
8 8 9 0

35

# notes
출발해 모든 v를 찍고 돌아올 예정. (가장 적은 비용으로)
항상 두 도시 사이에 길이 있는 건 아님

# strategy
음.. 일단 몇 가지 방법이 얼추 생각나긴 한다.
- 플로이드와샬 : 가는 길을 기록해야 하므로 써먹을 수 없겠다.
- 매 번 방문시마다 방문했단 걸 기록해야 할텐데 음 잘 모르겠다.

# pseudo code



'''


def tsp(dist_t):
    n = len(dist_t)
    VISITED_ALL = (1 << n) - 1
    dp_t = [[None] * (1 << n) for _ in range(n)]
    INF = float('inf')

    def find_path(last, visit_bits):
        if visit_bits == VISITED_ALL:
            return dist_t[last][0] or INF

        if dp_t[last][visit_bits]:  # 계산할 필요가 없다면 바로 리턴
            return dp_t[last][visit_bits]

        tmp = INF
        for city in range(n):
            city_bit = 1 << city
            # 해당 도시를 아직 방문하지 않는데 갈 수 있는 상황이라면
            if visit_bits & city_bit == 0 and dist_t[last][city] != 0: # 가장 적은 비용을 찾음.
                tmp = min(tmp, find_path(city, visit_bits | city_bit) + dist_t[last][city])
        dp_t[last][visit_bits] = tmp
        return tmp

    return find_path(0, 1 << 0)  # 0번부터 출발!

n = int(input())
dist_t = []
for _ in range(n):
    dist_t.append(list(map(int, input().split())))

print(tsp(dist_t))
