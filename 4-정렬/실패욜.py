def solution(N, stages):
    fail_rates = []
    stage_left = len(stages)
    
    for i in range(1, N+1):
        howmany = stages.count(i)
        if stage_left != 0:
            fail_rates.append((i, howmany/stage_left))
        else:
            fail_rates.append((i, 0))
        
        stage_left -= howmany
    
    print(fail_rates)
    answer = sorted(fail_rates, key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]