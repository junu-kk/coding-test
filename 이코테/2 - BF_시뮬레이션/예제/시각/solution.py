N = int(input())

whole_n = 3600*(N+1)
if N >= 3:
    without3_n = 45*45*N
else:
    without3_n = 45*45*(N+1)

print(whole_n-without3_n)
