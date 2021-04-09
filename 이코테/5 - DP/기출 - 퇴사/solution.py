from sys import stdin
input = stdin.readline

n = int(input().rstrip())
days_moneys = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
dp_t = [0]*n
for i in range(n-1, -1, -1):
    day, money = days_moneys[i]
    if i+day > n:  # 물리적으로 다 못끝내면 컨틴뉴
        continue
    # 이제 이 일이 가능은 한 셈인데, 어느 게 이득인지를 셈해야겠지.
    # 쌓아온 일을 유지하느냐,
