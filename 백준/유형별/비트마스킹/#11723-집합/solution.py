from sys import stdin
input = stdin.readline

# 범위가 정해져있는 set ==> 비트연산
bits = 0

n = int(input().rstrip())
for _ in range(n):
    cmd = input().rstrip()
    if cmd == 'all':
        bits = (1 << 20) - 1
    elif cmd == 'empty':
        bits = 0
    else:
        cmd, param = cmd.split()
        idx = int(param) - 1
        if cmd == 'add':
            bits |= (1 << idx)
        elif cmd == 'remove':
            bits &= ~(1 << idx)
        elif cmd == 'check':
            print(0 if bits & (1 << idx) == 0 else 1)
        elif cmd == 'toggle':
            # xor == 토글이라고 생각해줄수 있겠다.
            bits ^= (1 << idx)
