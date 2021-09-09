# 힙을 쓰는 이유는, 별도의 정렬이 없이도 SJF로 처리해야 하기 때문임.
from heapq import heappush, heappop

def solution(jobs: list):
    job_n = len(jobs)
    answer, cur_time, job_finish_n = 0, 0, 0

    prev_job_start_time = -1

    h = []

    # 작업을 모두 완료할때까지
    while job_finish_n < job_n:
        # 적절한 타이밍에 작업을 대기열에 넣고
        # (매번 모든 job들을 확인하는게 맞나 == 시작시간별로 각자 한번씩만 들어가기에 괜찮음.)
        for disk_in_time, running_time in jobs[job_finish_n:]:

            # 지금 스케줄러에서 처리하는 작업이 있는가? (그냥 값보단 약간 처리가능? 불린느낌으로 보면 될것같음)
            if prev_job_start_time < disk_in_time <= cur_time:
                heappush(h, (running_time, disk_in_time))



        # 대기열에 있는 작업들 중 가장 짧은 하나 해치우기. 대기열이 비어있다면 단순 1초 경과.
        if h:
            running_time, disk_in_time = heappop(h)
            # 지금 이 시작하는 작업시각을 기록하고
            prev_job_start_time = cur_time
            # 여기서 러닝타임만큼 달린다음에
            cur_time += running_time
            # 작업이 처리되는데 걸린 시간을(대기시간 포함) answer에 더해준다.
            answer += (cur_time - disk_in_time)
            job_finish_n += 1
        else:
            cur_time += 1

    return answer // job_n



print(solution([[0, 3], [1, 9], [2, 6]]))
