def solution(N, stages):
    fail_rates = []
    people_left = len(stages)
    
    for i in range(1, N+1): # 1~N스테이지까지 반복 
        howmany = stages.count(i) # 얼마나 많이 나오는지 센 후
        if people_left != 0: # 다 안끝났으면 적용하고
            fail_rates.append((i, howmany/people_left))
        else: # 다끝났으면 실패율 0이고
            fail_rates.append((i, 0))
        
        people_left -= howmany
    
    print(fail_rates)
    answer = sorted(fail_rates, key=lambda x: x[1], reverse=True) # 실패율 내림차순 정렬.
    return [i[0] for i in answer]