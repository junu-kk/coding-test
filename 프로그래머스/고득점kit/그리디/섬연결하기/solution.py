def find_root(parent_t, v):
    if parent_t[v] != v:
        parent_t[v] = find_root(parent_t, parent_t[v])
    return parent_t[v]

def union_vs(parent_t, v1, v2):
    v1_parent = find_root(parent_t, v1)
    v2_parent = find_root(parent_t, v2)
    
    if v1_parent < v2_parent:
        parent_t[v2_parent] = v1_parent
    else:
        parent_t[v1_parent] = v2_parent
    
def solution(n:int, es:list):
    parent_t = [i for i in range(n)]
    answer = 0
    for v1, v2, cost in sorted(es, key=lambda x:x[2]):
        if find_root(parent_t, v1) != find_root(parent_t, v2):
            union_vs(parent_t, v1, v2)
            answer += cost
    
    
    return answer
    

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))