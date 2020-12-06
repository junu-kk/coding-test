# 1부터 출발해 2 3 5 쭉 곱해나가기
n = int(input())

ugly = [0] * n # 못생수 리스트 겸 dp테이블, 0으로 초기화
ugly[0] = 1 # 첫번재 못생수는 1

i2 = i3 = i5 = 0 # 인덱스와
next2, next3, next5 = 2, 3, 5 # 곱셈값. 2 3 5가 뒤섞이며 곱해질 예정.

for l in range(1, n): # 1부터 쭉 갈건데
    ugly[l] = min(next2, next3, next5) # 곱셈값중 가장 작은 게 그 다음 못생수일거고
    if ugly[l] == next2: # 만약 곱셈2에 도달했다면
        i2 += 1 # 인덱스 하나 올려주고
        next2 = ugly[i2] * 2 # 거기에 2를 곱해준 게 다음 후보가 되는 식.
    if ugly[l] == next3: # 아래도 똑같.
        i3 += 1
        next3 = ugly[i3]*3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1]) # 맨 마지막 출력
