'''
# io
2 # 로프개수
10
15

20 # 위 로프들로 들 수 있는 물체의 최대 중량


# notes


# strategy
결국 10 * 2이기 때문에 그렇게 된것.
그러면 min(ropes) * rope_n이 결국 답 아닌가?
아닐수도있지.
1 100 100이면
담은 3이 아닌 200이니까.

그러면 정렬을 해주면
1 100 100이고
거꾸로 생각을 해주면 되겠다.
100 200 3이니까.
여기서 최댓값을 리턴해주면 되겠고만.

"정렬해볼까?" 라고 생각한 게 중요한 문제였다.
'''

rope_n = int(input())
ropes = sorted([int(input()) for _ in range(rope_n)], reverse=True)

answer = 0
for i in range(rope_n):
    answer = max(answer, ropes[i]*(i+1))

print(answer)

