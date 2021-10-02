'''
# io
6
10 40 80 #
30 60 60
50 80 70
70 100 100
90 120 40
110 140 50

180 # 회의를 진행할 수 있는 최대 인원

# notes


# strategy
dp_t를 i번째 회의까지 진행했을 떄 최대라고 생각하면 되겠다.

# pseudo code



'''


class Meeting:
    def __init__(self, st, end, ppl):
        self.st = st
        self.end = end
        self.ppl = ppl


n = int(input())
meetings = [Meeting(0, 0, 0)]
for _ in range(n):
    meetings.append(Meeting(*map(int, input().split())))

dp_t = [0] * (n + 1)
dp_t[1] = meetings[1].ppl
for i in range(2, n+1):
    dp_t[i] = max(dp_t[i-1], dp_t[i-2] + meetings[i].ppl)

print(dp_t[n])