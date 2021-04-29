def binary_search(nums, li, ri):
    while li <= ri:
        mi = (li+ri)//2
        if nums[mi] == mi:
            return mi
        elif nums[mi] > mi:
            ri = mi-1
        else:
            li = mi+1
    return -1


n = int(input())
nums = list(map(int, input().split()))
print(binary_search(nums, 0, n-1))
