original_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selectionSort(arr):  # 선택정렬 : 가장 작은 데이터를 선택해, 앞으로 swap
    for i in range(len(arr)):
        min_i = i  # 가장 작은 값의 인덱스. 나중에 i와 min_i를 swap하기 위함.
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


def insertionSort(arr):  # 삽입정렬 : 순서대로 적절한 위치에 삽입
    for i in range(len(arr)):
        # i 왼쪽 숫자들은 이미 정렬되어 있는 상태.
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]  # 역전되는 시점에서 swap만 해주면 된다.
            else:
                break

    return arr


def quickSort(arr):  # 퀵정렬 : 슉 슈룩 슈루루룩
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_arr = [x for x in tail if x <= pivot]
    right_arr = [x for x in tail if x > pivot]

    return quickSort(left_arr) + [pivot] + quickSort(right_arr)


def countSort(arr):  # 계수정렬 : 공간을 팔아 시간을 사는 정렬
    count = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    result = []
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)

    return result


# 결과 확인
print(selectionSort(original_array))
print(insertionSort(original_array))
print(quickSort(original_array))
print(countSort(original_array))

# 그치만 파이썬에선 다 필요없다
print(sorted(original_array))
