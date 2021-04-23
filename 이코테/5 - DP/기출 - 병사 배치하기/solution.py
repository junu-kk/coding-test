n = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()  # LIS 문제로 변환

dp_t = [1] * n  # 싹다 내림차여도 최소 자기자신이니 1로 초기화
for i in range(1, n):
    for j in range(i):  # i 직전까지
        if soldiers[j] < soldiers[i]:  # 순리대로 가고 있다면
            dp_t[i] = max(dp_t[i], dp_t[j] + 1)  # i를 보다 큰 값으로 골라주기.
