'''
# io
4 7
20 15 10 17

15 # 적어도 7미터의 나무를 얻기 위한 절단높이 최댓값

# notes
파라메트릭 서치 문제.
0과 20으로 시작하자.

# strategy


# pseudo code



'''
from sys import maxsize

n, m = map(int, input().split())
namus = list(map(int, input().split()))
l, r = 0, max(namus)
answer = maxsize
while l <= r:
    cut_loc = (l + r) // 2
    namu_get = 0
    for namu in namus:
        if namu > cut_loc:
            namu_get += namu - cut_loc

    '''
    사실상 이 부분이 파라메트릭 서치와 이분탐색을 가르는 부분일 것이다.
    이분탐색은 큰경우, 같은경우, 다른경우로 깔끔하게 나눌 수 있었지만
    여기선 조건을 달성하지 못한 경우와 조건을 달성하는 경우로 나눌 수 있다.
        달성하지 못한 경우 : 자명한 편이다.
        달성한 경우 : 의외로 이분탐색이랑 똑같이 해준다.
        그럼 정답은 무엇을 리턴하는가? : 달성하지 못한 경우 움직이는 값을 리턴한다.
    
    일단 위는 내 가설이므로 문제를 계속해서 풀어보자.
    '''
    if namu_get < m:
        r = cut_loc - 1
    else:  # 이 부분이 조금 까다롭다.
        l = cut_loc + 1



print(r)
