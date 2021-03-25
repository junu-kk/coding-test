from itertools import combinations
from sys import stdin
input = stdin.readline

vowels = ('a', 'e', 'i', 'o', 'u')
pw_alph_n, alph_n = map(int, input().split())

alphs = sorted(input().split())

for pw_comb in combinations(alphs, pw_alph_n):
    vowel_n = 0
    consonant_n = 0
    for pw_alph in pw_comb:
        if pw_alph in vowels:
            vowel_n += 1
        else:
            consonant_n += 1

    if vowel_n >= 1 and consonant_n >= 2:
        print(''.join(pw_comb))
