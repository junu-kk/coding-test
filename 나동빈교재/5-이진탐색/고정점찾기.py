def bs(array, start, end):
    if start>end:
        return None
    mid = (start+end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return bs(array, start, mid-1)
    else:
        return bs(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

gjj = bs(array, 0, n-1)

print(-1 if not gjj else gjj)