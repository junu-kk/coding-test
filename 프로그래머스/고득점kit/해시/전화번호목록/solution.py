# 접두어 있으면 false, 없으면 true
def solution(phone_book: list):
    n = len(phone_book)
    phone_book.sort()

    for i in range(n-1):
        jeopdu = phone_book[i]
        cmp = phone_book[i+1]
        jeopdu_l = len(jeopdu)
        if jeopdu == cmp[:jeopdu_l]:
            return False

    return True


print(solution(['123', '456', '789']))
