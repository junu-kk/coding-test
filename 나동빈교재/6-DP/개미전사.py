'''
dp는 결국 다 메모이제이션 활용하고, 그를 통한 맨 마지막 인덱스를 출력하는갑다.
'''

n = int(input())

foods = list(map(int, input().split()))

d = [0] * 100 # 

d[0] = foods[0] # 창고0
d[1] = max(foods[0], foods[1]) # 0, 1 중 털면 더 이득인 위치
for i in range(2, n): # 그 다음부턴
    d[i] = max(d[i-1], d[i-2] + foods[i]) # 창고 전값을 유지하거나, 전전값에 현 창고값을 더하거나.

print(d[n-1])