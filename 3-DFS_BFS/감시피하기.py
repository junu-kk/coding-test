from itertools import combinations
BLANK = 'X'; blanks = []
OBSTACLE = 'O'
TEACHER = 'T'; teachers = []
STUDENT = 'S'
caught = False

n = int(input())
graph = []



for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == TEACHER:
            teachers.append((i, j))
        if graph[i][j] == BLANK:
            blanks.append((i,j))
def gamsi(r, c, direction):
    if direction == 0: # 왼쪽감시
        while c >= 0:
            if graph[r][c] == STUDENT:
                return True
            if graph[r][c] == OBSTACLE:
                return False
            c -= 1
    if direction == 1: # 오른쪽감시
        while c < n:
            if graph[r][c] == STUDENT:
                return True
            if graph[r][c] == OBSTACLE:
                return False
            c += 1
    if direction == 2: # 아래감시
        while r >= 0:
            if graph[r][c] == STUDENT:
                return True
            if graph[r][c] == OBSTACLE:
                return False
            r -= 1
    if direction == 3: # 위감시
        while r < n:
            if graph[r][c] == STUDENT:
                return True
            if graph[r][c] == OBSTACLE:
                return False
            r += 1
    return False

def process():
    for r, c in teachers:
        for i in range(4):
            if gamsi(r, c, i):
                return True
    return False

found = False

for random_obstacles in combinations(blanks, 3):
    for r, c in random_obstacles:
        graph[r][c] = OBSTACLE
    if not process():
        found = True
        break
    for r, c in random_obstacles:
        graph[r][c] = BLANK

print('YES' if found else 'NO')

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