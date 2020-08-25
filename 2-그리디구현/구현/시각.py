# 전체에서 3 아예 안들어간 경우만 빼기
n = int(input())
answer = 60 * 60 * (n+1)

# 00 00 00 ~ n 59 59
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' not in str(h)+str(m)+str(s):
                answer -= 1

print(answer)