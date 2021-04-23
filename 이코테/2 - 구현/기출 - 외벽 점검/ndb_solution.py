from itertools import permutations
INF = int(1e9)


def solution(n, weaks, friends):
    weak_n = len(weaks)  # 약한 벽 개수
    friend_n = len(friends)  # 친구 수
    for i in range(weak_n):  # weaks 두배로 늘려주기 위함.
        weaks.append(n + weaks[i])
    answer = INF  # 최솟값 찾는 거니까 처음에 정답은 큰 수로 초기화

    #### 여기부터 메인 로직 ####
    for weak_start_idx in range(weak_n):  # 1. 어떤 벽부터 출발할지 완탐
        for friend_perm in permutations(friends):  # 2. 어떤 친구 순으로 출발할지 완탐
            #### 첫 친구 투입 ####
            friend_count = 1  # 일단 한 명 투입하는 걸로 시작하고
            # 그 친구는 시작벽위치~flag까지 수리를 담당하게 됨.
            flag = weaks[weak_start_idx] + friend_perm[friend_count-1]

            #### 이후 친구들 투입 ####
            # weak_start_idx부터 잰 모든 벽 인덱스에 대해 (친구를 중심으로 iterate하는게 아닌, weak 중심으로 iterate함.)
            for idx in range(weak_start_idx, weak_start_idx + weak_n):
                if flag < weaks[idx]:  # 플래그가 더 작다는 것은, 한명을 더 투입해야 하는 것을 의미.
                    friend_count += 1
                    if friend_count > friend_n:  # 친구 다썼다면 브레이크
                        break
                    flag = weaks[idx] + \
                        friend_perm[friend_count - 1]  # 투입 후 똑같이 진행
            answer = min(answer, friend_count)
    if answer > friend_n:
        return -1
    return answer
