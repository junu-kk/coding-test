from sys import stdin
input = stdin.readline

bupum_n = int(input())
bupums = sorted(list(map(int, input().split())))

giveme_n = int(input())
givemes = list(map(int, input().split()))


def binary_search(arr, target, li, ri):
    while li <= ri:
        mid_i = (li+ri)//2
        if arr[mid_i] == target:
            return True
        elif arr[mid_i] > target:
            ri = mid_i - 1
        else:
            li = mid_i + 1
    return False


for giveme in givemes:
    if binary_search(bupums, giveme, 0, bupum_n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
