from sys import stdin
input = stdin.readline

n = int(input().rstrip())
print(sorted(list(map(int, input().rstrip().split())))[(n-1)//2])
