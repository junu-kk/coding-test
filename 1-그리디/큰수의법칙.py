# 문제를 잘 읽자.
# m번 더하되 하나는 k를 넘지 못함.
n, m, k = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

# 큰거 k번
# 그다음거 1번
# 반복수
answer = nums[0] * (m // (k+1) * k) + nums[1] * (m // (k+1))
print(answer)