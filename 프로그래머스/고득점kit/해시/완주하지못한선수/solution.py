from collections import Counter


def solution(ps: list, cs: list):
    ps_dict = Counter(ps)
    cs_dict = Counter(cs)
    for name, count in cs_dict.items():
        ps_dict[name] -= count

    for name, count in ps_dict.items():
        if count == 1:
            return name


