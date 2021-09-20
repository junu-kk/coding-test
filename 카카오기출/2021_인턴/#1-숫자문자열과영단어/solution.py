'''
일단 영단어_숫자_dict 선언해놓고
문자열 첨부터 쫙 읽어가며
숫자일때 : 고대로 append
문자일때 : 임시문자열에 계속 더해가다가, 특정 영단어가 되었을때 숫자 어펜드하고 임시문자열 초기화

그리고 다 읽었으면 임시문자열 마지막으로 반환해주고 끝.

'''
d = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def solution(s: str):
    tmp_s = ''
    answer = []
    for c in s:
        if c.isalpha(): # 문자라면
            tmp_s += c
            if tmp_s in d:
                answer.append(str(d[tmp_s]))
                tmp_s = ''
        else: # 숫자라면
            answer.append(c)

    # 막처리
    if len(tmp_s) > 0:
        answer.append(d[tmp_s])

    return ''.join(answer)


print(solution('one4seveneight'))
