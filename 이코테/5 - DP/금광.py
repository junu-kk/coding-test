# DP테이블을 맵 그대로 사용하는 방식.
# dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) -> 리스트 범위 벗어나는지 체크 필요.

for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split())) # 우선 1차원으로 쭉 입력을 받음.

    # dp테이블 초기화
    dp = []
    idx = 0
    for i in range(n):
        dp.append(arr[idx:idx+m]) # 1차원 -> 2차원으로 바꿔줌.
        idx += m

    for j in range(1, m): # 각 행, 열에 대해
        for i in range(n): 
            if i == 0: 
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] += max(left_up, left_down, left)

        result = 0

        for i in range(n):
            result = max(result, dp[i][m-1])

        print(result)