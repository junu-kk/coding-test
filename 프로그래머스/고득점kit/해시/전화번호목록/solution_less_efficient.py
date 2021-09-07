# 접두어 있으면 false, 없으면 true
def solution(phone_book: list):
    n = len(phone_book)
    phone_book.sort(key=lambda x: len(x))

    for i in range(n-1):
        jeopdu = phone_book[i]
        jeopdu_l = len(jeopdu)
        for j in range(i+1, n):
            cmp = phone_book[j]
            if jeopdu == cmp[:jeopdu_l]:
                # print(i, j)
                return False

    return True


print(solution(['123', '456', '789']))
