# ~34

'''
구멍 0 칸막이 1
input
- rn cn
- 아이스크림 칸
output : 아이스크림 개수

음.. 상하좌우로는 풀릴 수 있을까? : 아니.. 다시 돌아가야 함.
전혀 모르겠다~~
교재봐도 살짝 아리까리.. 강의 다시 듣자.

tc : H모양(010 000 010)
'''

rn, cn = map(int, input().split())
jido = []
for _ in range(rn):
    jido.append(list(map(int, input())))

# r은 0~rn-1 / c는 0~cn-1
# jido가 곧 방문리스트.
def dfs(r, c):
    if r < 0 or r >= rn or c < 0 or c >= cn:
        return False
    
    if jido[r][c] == 0:
        jido[r][c] = 1
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r+1, c)
        dfs(r, c-1)
        return True
    return False


answer = 0

# 어차피 모든 점에 dfs해도 되겠구나!! 만약 갈데없으면 바로 땡이니.
for each_r in range(rn):
    for each_c in range(cn):
        # print(each_r, each_c)
        if dfs(each_r, each_c) == True:
            answer += 1

print(answer)