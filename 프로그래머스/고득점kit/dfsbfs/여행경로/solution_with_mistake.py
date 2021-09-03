from pprint import pprint


def solution(tickets):
    v_set = set()
    starting_vs = set()
    for ticket in tickets:
        v_from, v_to = ticket
        v_set.add(v_from)
        v_set.add(v_to)
        starting_vs.add(v_from)

    vn = len(v_set)
    v_i = dict()
    i_v = []
    for idx, v in enumerate(v_set):
        v_i[v] = idx
        i_v.append(v)


    # 사이즈 딱맞게 했음에 유의!
    graph = [[] for _ in range(vn)]
    for ticket in tickets:
        v_from, v_to = ticket
        graph[v_i[v_from]].append(v_i[v_to])

    for each in graph:
        each.sort()

    s = [v_i["ICN"]]
    visit_t = [False] * vn
    visit_t[v_i["ICN"]] = True
    answer = []
    while s:
        v = s.pop()
        answer.append(i_v[v])
        for adj_v in graph[v]:
            if not visit_t[adj_v]:
                s.append(adj_v)
                visit_t[adj_v] = True

    return answer



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
