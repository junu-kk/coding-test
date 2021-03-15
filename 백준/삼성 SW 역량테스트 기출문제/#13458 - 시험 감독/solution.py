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
