'''
<io>
(()[[]])([])
28 # 점수

[][]((])
0 # 입력이 올바르지 못한 경우

<notes>
() : 2
[] : 3
(X) : 2 * X
[X] : 3 * X

<strategy>
tmp_score 필요

스택으로 하나하나 쌓아가주면 될듯.
여는괄호 : append
닫는괄호
    top이랑 같은경우
        tmp_score에 곱해줌
        스택이 바닥난 경우 tmp_score answer에 더해줌
    top이랑 다른경우 : 바로 0 리턴 후 종료

'''
bs = input()
s = []
answer = 0
tmp_score = 1
b_dict = {
    '(':')',
    '[':']'
}
for i in range(len(bs)):
    b = bs[i]
    if b in ('(', '['):
        s.append(b)
    elif b in (')', ']'):
        tmp_score = 0
        tmp_i = len(s) - 1
        pop_count = 0
        while tmp_i >= 0:
            if type(s[tmp_i]) == int: # 숫자면 임시점수에 더해주고

                tmp_score += s[tmp_i]
                pop_count += 1
            elif b_dict[s[tmp_i]] != b: # 짝이 안맞으면 빠꾸
                print(0)
                exit()
            else: # 짝이 맞으면
                for _ in range(pop_count+1): # 숫자 + 1만큼 팝해주고
                    s.pop()
                if tmp_score == 0:
                    s.append(3 if b == ']' else 2)
                else:
                    s.append(tmp_score*3 if b == ']' else tmp_score*2)
                break
            tmp_i -= 1
        # 숫자 제외 마지막 괄호를 역순으로 찾아 짝이 안맞으면 빠꾸
        # 역순으로 찾는동안 숫자들은 더하기
        # 짝이 맞으면 더해준 숫자 * 괄호점수를 팝해준 뒤 어펜드
print(sum(s))

