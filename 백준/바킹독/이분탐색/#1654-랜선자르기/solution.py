'''
<io>
4 11 # 랜선 네개 가지고 있는데 11개 필요함.
802 # 현 랜선 길이들
743
457
539

200 # 만들 수 있는 랜선의최대 길이


<notes>


<strategy>
모르겠어서 해설 봄. 리드미 참조.
1 ~ 802
'''

n, goal_n = map(int, input().split())
lans = [int(input()) for _ in range(n)]

l, r = 1, max(lans)
while l <= r:
    m = (l + r) // 2
    tmp_lan_n = 0
    for lan in lans:
        tmp_lan_n += (lan // m)  # 해당 길이로 자르고 나머지는 버림

    if tmp_lan_n < goal_n:  # 기껏 잘랐는데 목표치만큼 안나온다면, 길이를 덜 해서 잘라야겠지.
        r = m - 1
    else:
        l = m + 1

print(r)
