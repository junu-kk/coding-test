# 풀이 실패!
# https://programmers.co.kr/learn/courses/30/lessons/42891
# def solution(foods, k):
#     food_n = len(foods)
#     i = 0
#     for _ in range(k+1):
#         if i == food_n:
#             i = 0
#         if foods[i] > 0:
#             foods[i] -= 1
#         else:
#             i += 1
#             continue
#         i += 1
#     for _ in range(food_n):
#         if i == food_n:
#             i = 0
#         if foods[i] > 0:
#             return i+1
#         i += 1
#     return -1


# print(solution([3, 1, 2], 5))
