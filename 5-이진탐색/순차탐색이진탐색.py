def sequentialSearch(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

    return n

def recursiveBinarySearch(array, target, start, end):
    if start > end: # 시작이 더 크다면 탐색을 할래야 할수가 없음.
        return None

    mid = (start+end) // 2

    if array[mid] == target: # 중간점에서 찾으면 중간인덱스 리턴
        return mid
    elif array[mid] > target: # 타겟이 작다면 왼쪽반 탐색
        return recursiveBinarySearch(array, target, start, mid - 1)
    else: # 타겟이 크다면 오른쪽반 탐색
        return recursiveBinarySearch(array, target, mid + 1, end)

    
def iterativeBinarySearch(array, target ,start, end):
    while start <= end: # 완전 쪼그라들때까지 위의 로직을 반복. start와 end값을 직접 변경하는 식으로.
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None # 다 쪼그라들었는데 못찾으면 None이지 뭐.

mixedArr = [9,3,4,1,6,8,5,2,7]
sortedArr = [1,2,3,4,5,6,7,8,9]

print(sequentialSearch(9, 5, mixedArr))
print(iterativeBinarySearch(sortedArr, 4, 0, len(sortedArr)-1) + 1)
print(recursiveBinarySearch(sortedArr, 4, 0, len(sortedArr)-1) + 1)