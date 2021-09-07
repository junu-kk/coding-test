def solution(clothes: list):
    otjang = dict()
    for _, type in clothes:
        if type in otjang:
            otjang[type] += 1
        else:
            otjang[type] = 1

    answer = 1
    print(otjang)
    for v in otjang.values():
        answer *= (v+1)

    return answer-1


print(solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
