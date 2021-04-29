from sys import stdin
input = stdin.readline

gn = int(input())
pn = int(input())
gate_available = [True]*gn
answer = 0

for _ in range(pn):
    plane = int(input())
    docked = False
    for i in range(plane-1, -1, -1):
        if gate_available[i]:
            docked = True
            gate_available[i] = False
            # print(f'{plane} docking to {i}')
            answer += 1
            break

    if not docked:
        break


print(answer)
