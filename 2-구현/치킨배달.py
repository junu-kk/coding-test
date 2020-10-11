'''
빈칸 / 치킨집 / 집 (0 1 2)

치킨거리 : 모든 치킨거리의 합.

output : m개만 남겼을 때 도시의 치킨 거리 최솟값.

combination 쓰면 될듯??
원래 2에서 각각의 경우마다 치킨 거리를 구하고
그 중 최솟값을 구하면 되지
'''
from itertools import combinations

def get_answer(combi):
    result = 0
    for jr, jc in jip: # 집집마다
        temp = 1e9
        for cr, cc in combi: # 콤비마다
            if temp > abs(jr-cr) + abs(jc-cc) # 거리 구해서 최솟값이면 갱신
                temp = abs(jr-cr) + abs(jc-cc)
        result += temp
    return result


n, m = map(int, input().split())
city = []
chicken, jip = [], []
for i in range(n):
    city.append(list(map(int, input().split())))

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            jip.append((r,c))
        elif city[r][c] == 2:
            chicken.append((r,c))

chickencombies = list(combinations(chicken, m))

answer = 1e9
for combi in chickencombies:
    temp_answer = get_answer(combi)
    if answer > get_answer(combi):
        answer = temp_answer

print(answer)


    
