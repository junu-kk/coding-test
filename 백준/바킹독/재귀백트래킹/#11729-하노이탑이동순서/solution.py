'''
<io>
3 # 원판이 세개라면

7 # 7번을 옮겨야함. 다음의 과정으로!
1 3
1 2
3 2
1 3
2 1
2 3
1 3

<notes>
재귀를 잘 활용하면 됨.

<strategy>
공책에 정리함.


'''
answer = []

def subsol(plate_n, sijak, ingyeo, dochak):
    if plate_n == 1:
        answer.append((sijak, dochak))
        return

    subsol(plate_n-1, sijak, dochak, ingyeo)
    answer.append((sijak, dochak))
    subsol(plate_n-1, ingyeo, sijak, dochak)

n = int(input())
subsol(n, 1, 2, 3)
print(len(answer))
for a, b in answer:
    print(a, b)