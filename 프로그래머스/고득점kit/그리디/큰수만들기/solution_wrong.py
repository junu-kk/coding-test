'''
그 숫자들로 최댓값 만드는 함수
'''
def solution(number:str, k:int):
    strange_list = sorted(list(enumerate(sorted(list(enumerate(list(number))), key=lambda x:x[1]))), key=lambda x:x[1][0])
    hi = []
    count = 0
    for size_power, enum in strange_list:
        idx, num = enum
        if size_power <= idx + k:
            if count == k:
                hi.append(enum)
                continue
            count += 1
        else:
            hi.append(enum)

    return sorted(hi, key=lambda x:x[0])




print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))