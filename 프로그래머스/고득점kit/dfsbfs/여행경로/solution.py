def solution(tickets:list):
    tickets.sort(reverse=True)
    # 와 미쳤다 정점이 int가 아닌 string일때 딕셔너리로 하는 방법이 있겠구나 그러네
    graph = dict()
    for v1, v2 in tickets:
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]

        if v2 not in graph:
            graph[v2] = []

    s = ['ICN']
    answer = []
    while s:
        v = s[-1]
        # 인접한게 없을 경우 스택을 소모해주고
        if len(graph[v]) == 0:
            answer.append(s.pop())
        # 인접한 경우 e를 소모해줌. -> 감은 오는데 완벽한 이해는 안됨.
        else:
            s.append(graph[v].pop())

    answer.reverse()
    return answer

