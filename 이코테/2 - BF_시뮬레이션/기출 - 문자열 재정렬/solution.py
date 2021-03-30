from sys import stdin
input = stdin.readline

alphs = []
num_sum = 0

s = input().rstrip()
for chr in s:
    if chr.isnumeric():
        num_sum += int(chr)
    else:
        alphs.append(chr)

print(''.join(sorted(alphs)), end='')
print(num_sum)
