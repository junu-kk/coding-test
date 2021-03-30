# 나동빈 풀이 참조함!

from heapq import heappush, heappop


def solution(foods, k):
    food_n = len(foods)
    if sum(foods) <= k:
        return -1

    q = []
    for i in range(food_n):
        heappush(q, (foods[i], i + 1))  # (음식양, 음식번호)

    '''
    전략
    1. 제일 작은 음식을 다 먹는다. 근데 그거 다 먹기 위해서 다른 것도 몇입씩 떼어 먹어야 한다.
    2. 그 다음 작은 음식을 다 먹기 위해선, (그 음식의 사이즈 - 아까 뜯어먹은 양)을 또 먹어야겠지? 이것 또한 그만큼 먹으며 다른 음식들도 그만큼 떼어먹는다.
    3. 반복한다.
    '''

    time_elapsed = 0  # 먹기 위해 사용한 총 시간
    prev_food_size = 0  # 반복문 보면 이게 어떻게 쓰이는지 알거임.

    # 가장 작은 음식을 다 먹을만큼 다른 음식에도 시간을 쓰는 것이 가능할 경우
    while time_elapsed + ((q[0][0]-prev_food_size)*food_n) <= k:
        food_size, i = heappop(q)  # 먹을준비
        time_elapsed += (food_size - prev_food_size) * food_n  # 쳐묵
        food_n -= 1  # 쳐묵완료
        prev_food_size = food_size  # 떼어먹은 만큼을 저장.

    # q는 힙이었지만 이제부턴 리스트다. 음식번호순으로 (남아있는) 음식 정렬 후
    result = sorted(q, key=lambda x: x[1])
    # 다 먹은거 제하고, 남은 시간 계산해서 순서가 찾아온 음식 리턴.
    return result[(k-time_elapsed) % food_n][1]
