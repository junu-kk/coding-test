'''
음.. 컨디션이 좋으면 다시 봐보자.
경로압축 기법을 사용했다고 한다.
https://chlee1001.github.io/2021/04/11/BAEKJOON-18869-21-04-11/
'''

import sys

input = sys.stdin.readline

space_n, planet_n = map(int, input().split())

space_list = [list(map(int, input().split())) for _ in range(space_n)]

new_space_list = [[] for _ in range(space_n)]
dict = {}
for i in range(space_n):
    new_list = sorted(list(set(space_list[i])))
    for j in range(len(new_list)):
        dict[new_list[j]] = j
    for x in (space_list[i]):
        new_space_list[i].append(dict[x])

new_space_list.sort()
cnt, ans = 1, 0
for i in range(1, space_n):
    if new_space_list[i] == new_space_list[i - 1]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        cnt = 1

ans += cnt * (cnt - 1) // 2
print(ans)
