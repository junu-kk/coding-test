#~10

'''

괴물없 1 괴물있 0
1로만 다녀서 끝까지 가야 하는 거구나.
bfs 돌리다가 n,m 다다르면 끝내면 되지 않을까?

input
n m
미로정보(공백x)

output
최소 이동 칸 수
'''

from collections import deque

# 그래프 준비
n,m=map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
print(graph)

# 방문리스트
visited = [[False]*m for _ in range(n)]
visited[0][0] = True

# bfs 함수
'''
1,1부터 n,n까지 dfs를 하는데
0이면 못감 1이면 감.
'''
def bfs(graph, r, c, visited):
    q = deque((r,c))
    visited[r][c] = True
    answer = 0
    while q:
        v = q.popleft()

        for each_v in [(v[0]-1,v[1]),(v[0],v[1]+1),(v[0]+1,v[1]),(v[0],v[1]-1)]:
            if each_v == (n,m):
                return answer
            if visited[each_v[0]][each_v[1]] == False:
                answer+=1
                q.append(each_v)
                visited[each_v[0]][each_v[1]] = True

        '''
        봐야 할 부분 : v[0]+-1, v[1]+-1
        '''
print(bfs(graph,0,0,visited))