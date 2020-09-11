# 나동빈 풀이 참조
'''
1. heapq 사용 : sort 없이 최솟값을 쭉쭉 빼내는게 장점.
    heapq.heappush(큐, 넣을거)
    heapq.heappop(큐)
    식으로 사용.
2. now와 previous를 사용해 요레 요레 한 게 괜찮네.
'''

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # (음식양, 음식번호)
    
    sum_value = 0 # 먹기 위해 사용한 총 시간
    previous = 0 # 직전에 다 먹은 음식 시간 (빨리먹는대로 차곡차곡 쌓임)
    length = len(food_times) # 남은 음식 수
    
    # k를 동낼때까지
    # 지금까지 먹은 시간에 음식을 끝장내는 마지막 바퀴까지
    while sum_value + ((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0] # 힙 맨 위에있는 최솟값 꺼내서
        sum_value += (now-previous) * length # 남은 음식 수만큼, 남은 만큼 먹고
        length -= 1 # 다 먹은음식 하나 빼주시고
        previous = now # 이전음식시간 재세팅
        
    result = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value) % length][1]