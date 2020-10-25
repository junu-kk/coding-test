'''
bl, br 복습
bl : 정렬된 리스트에 데이터를 삽입할 가장 왼쪽 인덱스
br : 정렬된 리스트에 데이터를 삽입할 가장 오른쪽 인덱스
sample = [1,2,4,4,8]
print(bl(sample), br(sample)) # 2 4
-> 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구할 때 효과적으로 사용됨.
'''

from bisect import bisect_left, bisect_right as bl, br

def count_by_range(array, lv, rv):
    ri = br(array, rv)
    li = bl(array, lv)
    return ri-li

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

print(-1 if count == 0 else count)