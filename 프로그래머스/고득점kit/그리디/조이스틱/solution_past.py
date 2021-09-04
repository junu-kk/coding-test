def solution(name):
    n = len(name)
    if n == 1:  # tc 하나가 통과 안되던데, 알고보니 이거였음.
        dist = abs(ord(name) - ord('A'))
        return min(dist, 26-dist)
    l_combo = r_combo = 0
    for i in range(1, n):
        if name[i] != 'A':
            break
        r_combo += 1

    for i in range(n-1, 0, -1):
        if name[i] != 'A':
            break
        l_combo += 1

    answer = n - 1 - max(l_combo, r_combo)
    for a in name:
        dist = abs(ord(a) - ord('A'))
        answer += min(dist, 26-dist)
    return answer