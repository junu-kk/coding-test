'''
input
N
각 공포도

출력은
여행떠날수있는그룹수최댓값

공포도 x면 반드시 x명 이상이어야 함.
소트하면 되는거 아님?

'''

N = int(input())
gps = sorted(list(map(int, input().split())), reverse=True)
i = 0
answer = 0
while i < N:
    answer += 1
    i += gps[i]
print(answer)