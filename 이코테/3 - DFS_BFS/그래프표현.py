# 1 --(가중치7)-- 0 --(가중치5)-- 2 그래프를 행렬과 연결리스트를 통해 표현하시오.

'''
075
70X
5X0
'''

INF = 1e9

graph_arr = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

graph_ll = [[] for _ in range(3)]
graph_ll[0].append((1, 7))
graph_ll[0].append((2, 5))
graph_ll[1].append((0, 7))
graph_ll[2].append((0, 5))

print(graph_arr)
print(graph_ll)