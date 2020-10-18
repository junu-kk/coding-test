'''
input
N
각 공포도

출력은
여행떠날수있는그룹수최댓값

공포도 x면 반드시 x명 이상이어야 함.
소트하면 되는거 아님?

TODO : 다시풀자!!!!
'''

N = int(input())
gps = sorted(list(map(int, input().split())), reverse=True)

more_people_please = 0
groupn = 0
for i in range(N):
    if more_people_please == 0:
        groupn += 1
        more_people_please = gps[i] - 1
    else:
        more_people_please -= 1

print(groupn)