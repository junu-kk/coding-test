from itertools import combinations

'''
<io>
group_n
people: i번째 시험장에 people[i]만큼의 사람이 있음.
links: i번째의 왼쪽 자식과 오른쪽 자식

<notes>

<strategy>
유니온-파인드~
각 link들을 저장해두고
거기서 group_n-1개만 취했을 때의 최댓값의 최소를 구하면 됨. (최대한 균등하게 나누어야.)

vn은 en+1만큼 있을 것이다. (MST이기 때문)
근데 거기서 group_n만큼 그룹을 만들고 싶으면, group_n-1개만큼의 간선을 빼면 된다.
이는 en-group_n+1만큼의 간선을 선택하면 되는 것과 같다.

각 links마다, -1이 아닌 부분에 한해 원래인덱스-값[0] 원래인덱스-값[1]을 계속 es에 어펜드해준다.
answer = INF
for comb in combinations(es,남길간선수):
    parent_t = [0] * vn
    for e in comb:
        유니온(e)
    power_dict = {}
    for v in range(vs):
        root = find_root(parent_t, v)
        if root in power_dict:
            power_dict[root] += people[v]
    answer = min(answer, max(power_dict.values()))
'''


def find_root(parent_t, v):
    if parent_t[v] != v:
        parent_t[v] = find_root(parent_t, parent_t[v])
    return parent_t[v]


def union_vs(parent_t, v1, v2):
    r1 = find_root(parent_t, v1)
    r2 = find_root(parent_t, v2)

    if r1 < r2:
        parent_t[r2] = r1
    else:
        parent_t[r1] = r2


def solution(group_n, people, links):
    '''
    각 links마다, -1이 아닌 부분에 한해 원래인덱스-값[0] 원래인덱스-값[1]을 계속 es에 어펜드해준다.
    answer = INF
    for comb in combinations(es,남길간선수):
        parent_t = [0] * vn
        for e in comb:
            유니온(e)
        power_dict = {}
        for v in range(vs):
            root = find_root(parent_t, v)
            if root in power_dict:
                power_dict[root] += people[v]
        answer = min(answer, max(power_dict.values()))
    '''
    INF = int(1e9)
    vn = len(people)
    es = []
    for v in range(vn):
        l, r = links[v]
        if l != -1:
            es.append((v, l))
        if r != -1:
            es.append((v, r))

    en_to_leave = len(es) - group_n + 1
    answer = INF
    for comb in combinations(es, en_to_leave):
        root_power_d = {}
        parent_t = [i for i in range(vn)]
        for v1, v2 in comb:
            union_vs(parent_t, v1, v2)
        for v in range(vn):
            root = find_root(parent_t, v)
            if root in root_power_d:
                root_power_d[root] += people[v]
            else:
                root_power_d[root] = people[v]

        answer = min(answer, max(root_power_d.values()))

    return answer