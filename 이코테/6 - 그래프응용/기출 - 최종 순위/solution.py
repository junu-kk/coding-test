from collections import deque

tc_n = int(input())
for tc in range(tc_n):
    team_n = int(input())
    ranks = list(map(int, input().split()))
    change_n = int(input())
    changes = list(map(int, input().split()))
