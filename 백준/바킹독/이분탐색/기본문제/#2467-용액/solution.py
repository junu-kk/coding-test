'''
# io
5
-99 -2 -1 4 98

-99 98 # 오름차순
# notes
산은 +, 알칼리는 -
가장 0에 가까운 용액을 만들려고 함.
같은 상성 섞기도 가능.
'정렬된 순서'로 주어짐.

# strategy
bf로 하면 젤 쉽긴 한데
투포인터로 해야하나?
    합이 양수일 경우 : 줄여야 하므로 오른쪽을 줄임.
    합이 음수일 경우 : 늘려야 하므로 왼쪽을 늘림.


# pseudo code



'''
n = int(input())
liqs = list(map(int, input().split()))
i, j = 0, n - 1
hubo = [0, n - 1]
while i < j:  # 두 용액은 겹칠 수 없으므로
    liq1, liq2 = liqs[i], liqs[j]
    mix = liq1 + liq2
    if mix == 0:
        print(liqs[i], liqs[j])
        exit()

    if abs(mix) < abs(liqs[hubo[0]] + liqs[hubo[1]]):
        hubo = [i, j]

    if mix > 0:  # 오른쪽을 줄이자.
        j -= 1
    elif mix < 0:  # 왼쪽을 늘리자.
        i += 1

print(liqs[hubo[0]], liqs[hubo[1]])
