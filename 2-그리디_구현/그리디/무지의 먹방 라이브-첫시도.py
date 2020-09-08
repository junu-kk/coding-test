'''
그리디
1 4 9 16 25라 하고 k가 대충 9라고 하자

다 먹었으면 -1 리턴

그렇지 않다면 (그리디하게 간다면)
    1 다먹고 4 다먹고 나머지 세개를 먹다 말거지.
    25-1-4=20이고 이걸 9 16 25가 뿜빠이하면 7 7 6
    즉 25를 먹을 차례인 것을 알 수 있다
    
정석으로 간다면
    [1,4,9,16,25] 무한반복
    0이면 스킵
    아니면 -1
    리턴은 i+1

'''


def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    eating_count = 0
    i = 0
    food_n = len(food_times)

    while eating_count < k:
        if food_times[i] != 0:
            food_times[i] -= 1
            eating_count += 1

        i += 1
        if i == food_n:
            i = 0

    return i+1
