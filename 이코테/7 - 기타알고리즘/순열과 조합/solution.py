from itertools import combinations, permutations

datas = [1, 2, 3]
print('**** permutations ****')
for perm in permutations(datas, 2):
    print(perm)
print('**** combinations ****')
for comb in combinations(datas, 2):
    print(comb)
