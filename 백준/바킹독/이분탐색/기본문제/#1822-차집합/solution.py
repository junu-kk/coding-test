'''
# io
4 3 # an bn
2 5 11 7 # as
9 7 4# bs


# notes
as-bs를 원소의 개수와 그 값을 오름차순으로 출력.
공집합이면 0 출력

# strategy


# pseudo code



'''

an, bn = map(int, input().split())
aset = set(map(int, input().split()))
bset = set(map(int, input().split()))
cha = aset-bset
if cha:
    print(len(cha))
    print(*sorted(list(cha)))
else:
    print(0)