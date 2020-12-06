# 가장 긴 증가하는 부분수열 문제 : 수열에서 증가하는 가장 긴 부분수열 찾기 (띄엄 포함)
# 모두 1로 초기화한 상태에서
# 점화식은 j<i일때 d[i] = max(d[i], d[j]+1) if array[j] < array[i]
n = int(input())
arr = list(map(int, input().split()))
arr.reverse() # 여기서 증가하는 가장 긴 부분수열을 찾으면 됨.

dp = [1] * n # 모두 1로 초기화한뒤
for i in range(1, n):
    for j in range(0, i): # j<i일때
        if arr[j] < arr[i]: # 증가하는 형태면
            dp[i] = max(dp[i], dp[j] + 1) # dp테이블은 위 점화식과 같게 되겠지.

print(n-max(dp)) # 전체에서 가장 긴 부분수열을 빼니까 빼야할 최소 병사수가 나오게 됨.