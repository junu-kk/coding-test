'''
<느낀점>
시도 1:
    쉬운 문제인데도 첫 시도에 실패함.
    그 이유를 보니 문제를 잘못 이해했음.
    쉬운 문제일수록 문제에 나온 TC를 돌려보는 것을 넘어서,
    정확히 문제를 이해했는지 재차 확인해봐야겠다.

시도 2:
    그리고 시도 2에서도 실패함
    효율적으로 고친다고 answer+= ... 부분을 고쳤다가 틀림.
    역시나 수학이 들어가는 경우에도 다양한 경우의 수를 고려해야겠다.

summary
총감은 only 1명
부감은 여러명(1명 이상임에 유의!!).

input
3 : 3개의 시험장
3 4 5 : 각 시험장엔 3, 4, 5명의 응시자
2 2 : 총감은 한번에 2명 감시ㄱㄴ, 부감은 한번에 2명 감시ㄱㄴ.

output
7 : 필요한 감독관 수의 최솟값은 7명

strategy
그리디네?

'''

from sys import stdin
input = stdin.readline

place_n = int(input())
ppl_ns = list(map(int, input().split()))
gamdok1, gamdok2 = map(int, input().split())
answer = place_n  # 일단 총감1 배치해놓고
for ppl_n in ppl_ns:
    left_ppl_n = ppl_n - gamdok1
    if left_ppl_n > 0:
        answer += ((left_ppl_n-1) // gamdok2)+1

print(answer)
