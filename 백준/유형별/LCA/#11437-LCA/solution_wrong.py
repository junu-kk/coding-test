'''
# io
15 # vn
1 2 # es
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6 # v_ssang_n
6 11 # v_ssangs
10 9
2 6
7 6
8 13
8 15

2 # 가장 가까운 공통 조상
4
2
1
3
1

# notes


# strategy
유파 : 연결을 끊어내는게 없으니 애매함.
위상정렬 : indegree에 해당하는 노드들을 set에 저장해주면, 풀 수 있을 것 같긴 함.
하지만 1-4-7이 서로 다른 depth에 있다면,

# pseudo code



'''

# 흠 왜 틀린거지
vn = int(input())
indegree_t = [set([v]) for v in range(vn + 1)]
for v in range(1, vn+1):
    indegree_t[v].add(1)

es = []
for _ in range(vn - 1):
    es.append(sorted(map(int, input().split())))

for v1, v2 in sorted(es):
    # 큰 셋에 작은 부모가 들어가야함.
    indegree_t[v2] |= indegree_t[v1]

v_ssang_n = int(input())
for _ in range(v_ssang_n):
    v1, v2 = map(int, input().split())
    print(max(list(indegree_t[v1] & indegree_t[v2])))
