from collections import deque


def solution(brd_l: int, brd_max_w: int, tr_ws: list):
    q = deque(tr_ws)
    brd_w_ts = []
    answer = 0

    # 큐도 비고 다리도 빌때까지 반복
    while q or brd_w_ts:
        #  print(brd_w_ts)
        # 다리에 트럭이 있다면 직진
        for i in range(len(brd_w_ts)):
            brd_w_ts[i][1] += 1

        # 다 건넌 트럭이 있다면 빼주고
        brd_w_ts = [brd_w_t for brd_w_t in brd_w_ts if brd_w_t[1] < brd_l]

        # 현재 다리에 올라간 트럭 무게를 구해주고
        w_status = 0
        for i in range(len(brd_w_ts)):
            w_status += brd_w_ts[i][0]

        # 넣을 수 있다면 넣고
        if q:
            w = q.popleft()
            if w + w_status <= brd_max_w:
                brd_w_ts.append([w, 0])
            else:
                q.appendleft(w)

        # 시간 올리기
        answer += 1

    return answer


# #  print(solution(2, 10, [7, 4, 5, 6]))
# #  print(solution(100, 100, [10]))
#  print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
