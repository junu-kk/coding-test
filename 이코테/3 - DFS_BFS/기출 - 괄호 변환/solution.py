def preprocessing(s):
    if len(s) == 0:
        return s
    balance = 1 if s[0] == '(' else -1
    for i in range(1, len(s)):  # 인덱스로 나눌 예정
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            break
    return i+1


def correct(s):
    left_b_n = 0
    for b in s:
        if b == '(':
            left_b_n += 1
        elif b == ')':
            if left_b_n == 0:
                return False
            left_b_n -= 1
    return True


def solution(s: str):
    i = preprocessing(s)

    else:
