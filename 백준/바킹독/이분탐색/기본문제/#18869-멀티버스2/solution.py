'''
음.. 컨디션이 좋으면 다시 봐보자.
경로압축 기법을 사용했다고 한다.
https://chlee1001.github.io/2021/04/11/BAEKJOON-18869-21-04-11/

사실 제대로 이해는 안됐는데 일단 그러려니 싶다.
'''

import sys

input = sys.stdin.readline

space_n, planet_n = map(int, input().split())

spaces = [list(map(int, input().split())) for _ in range(space_n)]

new_space_list = [[] for _ in range(space_n)]
dict = {}
for spi in range(space_n):
    new_list = sorted(list(set(spaces[spi]))) # 중복제거되고 정렬된 우주
    for pli in range(len(new_list)):
        dict[new_list[pli]] = pli # 행성: 인덱스 형태로 딕셔너리에 담고
    for pli in (spaces[spi]): # 이제 진짜 우주와 비교하며
        new_space_list[spi].append(dict[pli]) # 중복제거 인덱스들을 담는다.

new_space_list.sort() # 정렬 때려주시고
cnt, answer = 1, 0
for spi in range(1, space_n):
    if new_space_list[spi] == new_space_list[spi - 1]: # 중복될때마다 카운트 늘려주고
        cnt += 1
    else: # 중복 안되면 정산 후 카운트 리셋
        answer += cnt * (cnt - 1) // 2
        cnt = 1

answer += cnt * (cnt - 1) // 2 # 마지막 처리
print(answer)