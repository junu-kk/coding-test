# 그래 일단 이 정도만 알아두자..

def solution(n, m):
    s = []

    def dfs():
        if len(s) == m:
            print(' '.join(map(str, s))) # 깊이깊이 들어가서 겨우 하나 프린트
            return

        for i in range(1, n + 1): # 백트래킹의 기본
            if i not in s: # 시도하지 않았다면
                s.append(i) # 간보고
                dfs() # 재귀돌리고
                s.pop() # 빠진다

    dfs()


solution(4, 2)
