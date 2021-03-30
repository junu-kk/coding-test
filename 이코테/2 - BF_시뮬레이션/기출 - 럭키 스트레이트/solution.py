from sys import stdin
input = stdin.readline

num = input().rstrip()
l = len(num)
num1 = num[:l//2]
num2 = num[l//2:]

if sum(map(int, num1)) == sum(map(int, num2)):
    print('LUCKY')
else:
    print('READY')
