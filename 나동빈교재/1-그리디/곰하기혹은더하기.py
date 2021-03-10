'''
곱하기 더하기 넣어서, 무조건 왼쪽에서 순서대로 이뤄지는 연산 중 ㄱㄱ하기.
0 : 더하자
1 : 더하자
'''

num = input()
answer = int(num[0])
for i in range(1, len(num)):
    if i == '0' or i == '1' or answer == 0 or answer == 1:
        answer += int(num[i])
    else:
        answer *= int(num[i])

print(answer)