'''
연속된 숫자 한번에 뒤집기
크게 10101 일 거 아녀.
그러면 
'''
n = input()
now = n[0]
count_0 = 0
count_1 = 0
if now == '0':
    count_0 += 1
else:
    count_1 += 1

'''
바뀌는 부분을 어케 잡아낼까~
'''

for i in n:
    if now == i:
        continue
    elif i == '0':
        count_0 += 1
        now = '0'
    else:
        count_1 += 1
        now = '1'

print(min(count_0, count_1))