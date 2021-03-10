# 답지를 많이 참고했습니다 ^^.. 위상정렬을 써야하는 개념은 이해함!

from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for i in range(n+1)]
    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a]-=1
            indegree[b]+=1
    
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
            
        if len(q) >= 2:
            certain = False
            break
            
        now = q.popleft()
        result.append(now)

        for i in range(1, n+1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    
    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()
