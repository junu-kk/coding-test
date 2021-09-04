def solution(number:str, k:int):
    s = []
    for num in number:
        while s and s[-1] < num and k > 0:
            k -= 1
            s.pop()
        s.append(num)


    return "".join(s[:len(s)-k])


print(solution())