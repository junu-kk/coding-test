def solution(numbers:list):
    str_nums = list(map(str, numbers))
    str_nums.sort(key=lambda x:x*3, reverse=True)

    return str(int(''.join(str_nums)))


print(solution([6,10,2]))

