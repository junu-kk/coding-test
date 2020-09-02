'''

괴물없 1 괴물있 0
1로만 다녀서 끝까지 가야 하는 거구나.
bfs 돌리다가 n,m 다다르면 끝내면 되지 않을까?

input
n m
미로정보(공백x)

output
최소 이동 칸 수

왜 9가 나오지??
왜 다음의 경우 0이 나오지?
11111
00101
01101
01001
01111

'''

from collections import deque

# 그래프 준비
n,m=map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
print(graph)

# 방문리스트 : graph가 곧 방문리스트이기에 필요 없다.

# 방향벡터
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# bfs 함수
'''
1,1부터 n,n까지 dfs를 하는데
0이면 못감 1이면 감.
'''
# 어차피 graph와 방문리스트는 전역이니까 굳이 안넣어줘도 됨.
# 그리고 여기선 방문리스트가 그래프라서 괜춘.
def bfs(r,c):
    q = deque()
    q.append((r,c))
    
    while q:
        # 이런 코드를 짜야한다 싶으면 방향벡터 활용하자.
        # for each_v in [(v[0]-1,v[1]),(v[0],v[1]+1),(v[0]+1,v[1]),(v[0],v[1]-1)]:
        r, c = q.popleft()

        for i in range(4):
            dest_r = r + dr[i]
            dest_c = c + dc[i]

            # 범위를 벗어났거나 벽인 경우 다음 루프로.
            if dest_r >= n or dest_r < 0 or dest_c >= m or dest_c < 0 or graph[dest_r][dest_c] == 0:
                continue
            
            # 그렇지 않다면.. 방문하지 않은 경우만 최단거리 기록
            if graph[dest_r][dest_c] == 1:
                graph[dest_r][dest_c] = graph[r][c] + 1
                q.append((dest_r, dest_c))
    
    return graph[r-1][c-1]
        
print(bfs(0,0))