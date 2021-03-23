# 삽입 정렬
## 구현방법
1. 오른쪽 정렬안된부분 맨 앞을 골라 왼쪽 정렬된 부분에 삽입한다.
2. 두번째부터 n번째까지 1을 반복.

## 구현코드
```python
def insertion_sort(n):
    for i in range(1, n): # 오른쪽 정렬안된부분 맨 앞을 골라
        for j in range(i, 0, -1): # 왼쪽 정렬된 부분에 삽입을 할건데
            if arr[j] < arr[j-1]: # 오른쪽부터 정렬될때까지 swap이구나.
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
```

## 특징
* 시간복잡도 $O(n^2)$
* 이미 정렬된 형태라면 매우 빠르게 동작함.