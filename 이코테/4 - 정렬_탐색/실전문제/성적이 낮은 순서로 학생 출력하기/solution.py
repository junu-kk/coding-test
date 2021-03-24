from sys import stdin
input = stdin.readline

n = int(input())
name_scores = []
for _ in range(n):
    name, age = input().split()
    name_scores.append((name, int(age)))

# for name_score in sorted(name_scores, key=lambda x: x[1]):
#     name, score = name_score
#     print(name, end=' ')


def quick_sort(start_i, end_i):
    if start_i >= end_i:
        return

    pi, li, ri = start_i, start_i+1, end_i

    while li <= ri:
        while li <= end_i and name_scores[li][1] <= name_scores[pi][1]:
            li += 1
        while ri > start_i and name_scores[pi][1] <= name_scores[ri][1]:
            ri -= 1

        if li <= ri:
            name_scores[li], name_scores[ri] = name_scores[ri], name_scores[li]
        else:
            name_scores[ri], name_scores[pi] = name_scores[pi], name_scores[ri]

    quick_sort(start_i, ri-1)
    quick_sort(ri+1, end_i)


quick_sort(0, n-1)
print(name_scores)
