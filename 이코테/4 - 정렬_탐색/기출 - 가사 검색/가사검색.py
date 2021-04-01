from bisect import bisect_left, bisect_right as bl, br

def count_by_range(a, lv, rv): # fro??이면 froaa~frozz 단어개수 세주는 함수.
    ri = br(a, rv)
    li = bl(a, lv)
    return ri-li

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word) # 정순으로 찾는용
        reversed_array[len(word)].append(word[::-1]) # 역순으로 찾는용

    for i in range(10001): # 모든 값들을 문자열순으로 정렬. 둘 다 물음표는 마지막에 몰릴 거다.
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: # 쿼리별로
        if q[0] != '?': # 물음표가 뒤에있는 형태면
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z')) # fro??, froaa, frozz
        else: # 물음표가 앞에있는 형태면
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z')) # 그 반대.
        answer.append(res)
    return answer