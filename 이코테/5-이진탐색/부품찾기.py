# ~4 10
'''
input
N
N개의 정수
M
M개의 정수

process
이진탐색 안쓰면 진짜 쉬운데..
이진탐색을 쓴다면?
bupums가 정렬된 상태여야 하는데
음... sort 쓰면 nlogn들고
거기서 이진탐색 쓰면 logn 들어서
시간복잡도 (N+M)logN 됨.

결국 이진탐색 코드를 외워야하는게 맞구나 ㅇㅇ.

근데 그냥 아싸리 한다면
n^2니까..

output
yes / no

답지 보니까 계수정렬로도, set함수로도 풀 수 있다고 나오네.
'''

def easySolution():
    n = int(input())
    bupums = list(map(int, input().split()))
    m = int(input())
    jumuns = list(map(int, input().split()))
    for jumun in jumuns:
        if jumun in bupums:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def binarySearch(array, target, start, end):
    if start > end: # 시작이 더 크다면 탐색을 할래야 할수가 없음.
        return False

    mid = (start+end) // 2

    if array[mid] == target: # 중간점에서 찾으면 중간인덱스 리턴
        return True
    elif array[mid] > target: # 타겟이 작다면 왼쪽반 탐색
        return binarySearch(array, target, start, mid - 1)
    else: # 타겟이 크다면 오른쪽반 탐색
        return binarySearch(array, target, mid + 1, end)

n = int(input())
bupums = sorted(list(map(int, input().split())))
m = int(input())
jumuns = list(map(int, input().split()))
for jumun in jumuns:
    if binarySearch(bupums, jumun, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')