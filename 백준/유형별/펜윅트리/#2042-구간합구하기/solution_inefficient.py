'''
# io
5 2 2 # 숫자개수, 변경횟수, 합구하기횟수
1 # 숫자들
2
3
4
5
1 3 6 # 3번째를 6으로 변환
2 2 5 # 2번째부터 5번째까지 합 구하기
1 5 2
2 3 5


# notes
1 : 변환
2 : 구간합

# strategy


# pseudo code



'''
# 당연히 이렇게 짜면 통과못한다
num_n, change_n, sum_n = map(int, input().split())
nums = [int(input()) for _ in range(num_n)]
for _ in range(change_n+sum_n):
    cmd, i, j = map(int, input().split())
    if cmd == 1:
        # 변환
        nums[i-1] = j
    elif cmd == 2:
        # 구간합
        print(sum(nums[i-1:j]))