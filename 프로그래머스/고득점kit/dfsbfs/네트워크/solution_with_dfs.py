# CON = 1
# CONX = 0
#
#
# def dfs(adj_mtrx, v_start, visit_t, vn):
#     visit_t[v_start] = True
#     s = [v_start]
#
#     while s:
#         v1 = s.pop()
#         for v2 in adj_mtrx[v1]:
#             if adj_mtrx[v1][v2] == CON and (not visit_t[v2]):
#                 visit_t[v2] = True
#                 s.append(v2)
#
#
#
# def solution(vn:int, adj_mtrx:list):
#     visit_t = [False] * vn
#     answer = 0
#
#     s = [0]
#     visit_t[0] = True
#
#     while s:
#         v1 = s.pop()
#         for v2 in adj_mtrx[v1]:
#             if adj_mtrx[v1][v2] == CON
#
#     for v1 in range(vn):
#
#         if not visit_t[v]:
#             answer += 1
#             dfs(adj_mtrx, v, visit_t, vn)
#
#
#     return answer
#
#
# print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))