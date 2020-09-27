# 답지참조함. 조금은 생각해볼만한 그리디 문제.

n = int(input())
coins = sorted(list(map(int, input().split()))) # 오름차순 정렬
target_money = 1 # 만들 수 있는지없는지 확인할 타겟금액

for coin in coins: # 아래의 처리를 각 코인마다 확인(오름차순 정렬되어있다!)
    if target_money < coin: # 젤 작은 코인보다 target이 작으면? 만들수없는거지.
        break
    target_money += coin # 하지만 작지 않다면, 일단 그 코인만큼은 만들 수 있다는 뜻!

print(target)