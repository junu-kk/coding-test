# 각 행에서 가장 낮은걸 뽑는데 그 중 가장 큰거

# 2차원 배열 입력받기 정석
n , m = map(int, input().split())
cards=[]
for i in range(n):
    cards.append(list(map(int, input().split())))

answer = min(cards[0])
for row in cards:
    if min(row) > answer:
        answer = min(row)

print(answer)