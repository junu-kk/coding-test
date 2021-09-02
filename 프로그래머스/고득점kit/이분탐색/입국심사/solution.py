# 해설
def solution(n, times):
    l = 0
    r = max(times) * n # 여기까지는 내 아이디어와 비슷함.

    while l<r:
        mid = (l+r) // 2
        total = 0

        '''
        mid는 처음에 30이고
        t는 각각 7, 10이니까
        4와 3이 되겠네.
        '''
        for t in times:
            total += mid // t

        if total >= n:
            r = mid
        else:
            l = mid + 1

    return l

