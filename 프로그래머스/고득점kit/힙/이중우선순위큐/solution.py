from heapq import heappush, heappop


def solution(cmds: list):
    q = []

    for cmd in cmds:
        if cmd[0] == 'I':
            v = int(cmd.split()[1])
            q.append(v)
        elif cmd[0] == 'D' and q:
            if cmd.split()[1] == '1':  # 최댓값 삭제
                q.pop(q.index(max(q)))
            else:  # 최솟값 삭제
                q.pop(q.index(min(q)))

    if q:
        return [max(q), min(q)]
    else:
        return [0, 0]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
