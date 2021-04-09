from itertools import combinations
from sys import stdin
input = stdin.readline

BLANK = 0
HOME = 1
CHICKEN = 2

minimum_city_chicken_length = int(1e9)


def get_minimum_chicken_length(home_loc, chicken_locs):
    minimum_chicken_length = int(1e9)
    for chicken_loc in chicken_locs:
        minimum_chicken_length = min(minimum_chicken_length, abs(
            home_loc[0]-chicken_loc[0])+abs(home_loc[1]-chicken_loc[1]))
    return minimum_chicken_length


n, chicken_max_n = map(int, input().rstrip().split())
chicken_locs = []
home_locs = []
for r in range(n):
    row = list(map(int, input().rstrip().split()))
    for c in range(n):
        if row[c] == HOME:
            home_locs.append((r, c))
        elif row[c] == CHICKEN:
            chicken_locs.append((r, c))

for comb in combinations(chicken_locs, chicken_max_n):
    city_chicken_length = 0
    for home_loc in home_locs:
        city_chicken_length += get_minimum_chicken_length(home_loc, comb)
    minimum_city_chicken_length = min(
        minimum_city_chicken_length, city_chicken_length)

print(minimum_city_chicken_length)
