from sys import stdin
input = stdin.readline

n = int(input())
ppl = sorted(list(map(int, input().split())), reverse=True)
answer = 1
member_n, member_max_n = 1, ppl[0]

for i in range(1, n):
    if member_n < member_max_n:
        member_n += 1
    else:
        member_n = 0
        member_max_n = ppl[i]
        answer += 1

print(answer)
