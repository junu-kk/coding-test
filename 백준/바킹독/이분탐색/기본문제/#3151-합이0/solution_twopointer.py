# 풀이참조 : https://baby-ohgu.tistory.com/32
import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0
# 한 개의 수 선택 후 투 포인터를 통해 나머지 두개의 수 구하기
for i in range(n - 2):
    l, r = i + 1, n - 1 # i의 오른쪽과 맨 끝으로 투포인터
    goal = -nums[i] # 그치.. 합이 이게 되야하니.
    mx_idx = n
    while l < r:
        lnum, rnum = nums[l], nums[r]
        tmp = nums[l] + nums[r]
        if tmp < goal:
            l += 1
        elif tmp > goal:
            r -= 1
        else: # 합이 0인 경우
            if lnum == rnum: # 같은 수라면 br-bl처럼 단순 위치만 비교해주면 됨
                answer += r - l
            else: # 다른 수라면..
                if mx_idx > r:
                    mx_idx = r
                    while mx_idx >= 0 and nums[mx_idx - 1] == nums[r]:
                        mx_idx -= 1
                answer += r - mx_idx + 1
            l += 1 # 매우 중요.
print(answer)