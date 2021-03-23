'''
짝이 맞지 않는 괄호

1균형잡힌 -> 2올바른
스택쓰는것같은데?

1. 비었으면 빈거반환
2. w -> u(최소), v(아무거나)
u가 올바르다면?
    v재귀
올바르지 않다면
    ( + v재귀 + ) + u앞뒤제거괄호뒤집

'''
def is_ol(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True

def get_slicepoint(s): # 균형잡힌 괄호 문자열까지의 자르는 그 포인트를 리턴
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
    


def recursiveSolution(p):
    if len(p) == 0:
        return p
    
    slicepoint = get_slicepoint(p)
    u = p[:slicepoint+1]
    if slicepoint == len(p)-1:
        v = ''
    else:
        v = p[slicepoint+1:]
        
    if is_ol(u):
        return u + recursiveSolution(v)
    else:
        adding = ''
        for alph in u[1:-1]:
            if alph=='(':
                adding += ')'
            else:
                adding += '('
            # adding += '(' if alph == ')' else ')'
        
        return '(' + recursiveSolution(v) + ')' + adding

def solution(p):
    if is_ol(p):
        return p
    return recursiveSolution(p)

print(solution("(()())()"))
print(solution(')('))
print(solution("()))((()"))