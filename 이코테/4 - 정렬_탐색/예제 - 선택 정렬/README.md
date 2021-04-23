# 선택 정렬
## 구현방법
1. 오른쪽 정렬안된부분에서 가장 작은 걸 골라, 그 부분 맨 앞과 swap한다.
2. 첫번째부터 n번째까지 1을 반복.

## 구현코드
```python
def selection_sort(n):
    for i in range(n):  # i : 오른쪽 정렬안된부분의 맨 앞
        minv_i = i  # minv_i : 오른쪽 정렬안된부분의 가장 작은 값의 인덱스
        for j in range(i+1, n):  # j는 오른쪽 정렬안된부분을 훑는 인덱스
            if arr[minv_i] > arr[j]:
                minv_i = j
        arr[i], arr[minv_i] = arr[minv_i], arr[i] # 스왑
```

## 특징
* 시간복잡도 O(n<sup>2</sup>)
* 가장 생각하기 간단함.