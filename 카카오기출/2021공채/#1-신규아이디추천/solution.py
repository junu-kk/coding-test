'''
<io>


<notes>
규칙에 어긋난 아이디를 맞는걸로 추천해야 함.
3자 이상 15자 이하
소문자 숫자 - _ .
.는 처음 끝 연속 X

단계가 다 나와있음.
1. 대문자를 소문자로
2. 허용안되는 문자들 제거
3. 두번연속 나오는 마침표 하나로 합침
4. 처음이나 끝에 있는 마침표 제거
5. 다 날라갔다면 a 대입
6. 15자만 남기고, 끝에 . 없을때까지 제거
7. 1자라면 *3, 2자라면 *2[:3]

<strategy>
그낭 그대로 구현하면 됨.

'''


def c_ok(c: str):
    if c.islower() or c.isnumeric() or c in ('-', '_', '.'):
        return True
    return False


def solution(s: str):
    l = [c.lower() if c.isupper() else c for c in s]
    temp = []
    for c in l:
        if c_ok(c):
            temp.append(c)
    # print('12단계 후')
    # print(''.join(temp))
    l = temp
    temp = []
    combo = False
    for c in l:
        if c == '.' and not combo:
            combo = True
            temp.append('.')
        elif c != '.' and combo:
            combo = False
            temp.append(c)
        elif c != '.' and not combo:
            temp.append(c)
    # print('3단계 후')
    # print(''.join(temp))
    l = temp

    if l and l[0] == '.':
        l = l[1:]
    if l and l[-1] == '.':
        for i in range(len(l) - 1, -1, -1):
            if l[i] != '.':
                break
        l = l[:i + 1]

    if len(l) == 0:
        l = ['a']

    # print('45단계 후')
    # print(''.join(l))

    if len(l) > 15:
        for i in range(14, -1, -1):
            if l[i] != '.':
                break
        l = l[:i + 1]

    if len(l) == 1:
        l = l * 3
    elif len(l) == 2:
        l.append(l[1])

    return ''.join(l)


# print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
