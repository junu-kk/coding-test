'''
다른사람 풀이를 많이 참조하긴 했다.
dp인데 시작/종료시각을 바로 인덱스로 두지 않고,
번호를 매겨 정렬한 걸 인덱스로 둔 점이 인상깊다.
'''
n = int(input())
meetings = []
timelist = set()

for i in range(n):
    st, end, ppl = map(int, input().split())
    timelist.add(st)
    timelist.add(end)
    meetings.append([st, end, ppl])

timelist = sorted(list(timelist))
convert_d = dict()
for i in range(len(timelist)):
    convert_d[timelist[i]] = i  # 시작, 종료시간 순서대로 번호를 달아준 셈

for i in range(n):
    st, end = meetings[i][0], meetings[i][1]
    meetings[i][0] = convert_d[st]
    meetings[i][1] = convert_d[end]

meetings.sort(key=lambda x: x[1])  # 미팅도 종료시각순으로 정렬해주시고


dp_t = [0] * len(timelist) # dp_t는 각 시각까지의 인원 최댓값임.
prev_t = 0
for st, end, ppl in meetings:
    for i in range(prev_t + 1, end + 1): # 그 전 끝날때부터 지금 끝날때까지
        dp_t[i] = max(dp_t[i], dp_t[i - 1]) # 쭉 dp_t를 갱신해온 후 (중간중간 겹쳐있을 수 있기때문에 max로 갱신해줘야함.)
    dp_t[end] = max(dp_t[end], dp_t[st] + ppl) # 지금 미팅을 하느냐 마느냐 중 큰값으로 반영
    prev_t = end

print(dp_t[len(timelist) - 1])
