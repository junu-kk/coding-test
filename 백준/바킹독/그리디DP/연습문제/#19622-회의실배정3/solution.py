'''
회의실배정2와 뭐가 다른지 모르겠다.



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