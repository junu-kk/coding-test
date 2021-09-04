from itertools import permutations


def is_prime(param):
    if param < 2:
        return False

    for i in range(2, int(param**0.5) + 1):
        if param % i == 0:
            return False

    return True


def solution(numbers:str):
    answer_set = set()
    for l in range(1, len(numbers)+1):
        # numbers 중 l개를 뽑아 줄세울 것임
        for perm in permutations(numbers, l):
            num = int(''.join(perm))
            if is_prime(num):
                answer_set.add(num)


    print(answer_set)
    return len(answer_set)


print(solution("17"))
print(solution("011"))