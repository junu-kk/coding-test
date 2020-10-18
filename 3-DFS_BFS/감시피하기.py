# BLANK = 'X'
# OBSTACLE = 'O'
# TEACHER = 'T'
# STUDENT = 'S'
# caught = False
# n = int(input())
# graph = []
# after_graph = []
# for i in range(n):
#     graph.append(list(input().split()))


# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# def gamsi_student(r, c):
#     for i in range(4):
#         newr = r + dr[i]
#         newc = c + dc[i]
#         while 0 <= newr < n and 0 <= newc < n:
#             if after_graph[newr][newc] == BLANK:
#                 after_graph[newr][newc] = TEACHER
#             elif after_graph[newr][newc] == STUDENT:
#                 return True
#     return False

# def dfs(on):
#     global result

#     if on == 3:
#         for i in range(n):
#             for j in range(n):
#                 after_graph[i][j] = graph[i][j]
#         for i in range(n):
#             for j in range(n):
#                 if after_graph[i][j] == TEACHER:
#                     if gamsi_student(i, j):
#                         caught = True
#                         return
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == BLANK:
#                 graph[i][j] = OBSTACLE
#                 on += 1
#                 dfs(on)
#                 graph[i][j] = BLANK
#                 on -= 1

# dfs(0)
# print(caught)