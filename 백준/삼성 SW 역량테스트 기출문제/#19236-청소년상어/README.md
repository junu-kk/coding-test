```python
'''
# notes
4*4, 물고기는 번호와 방향을 가짐.
0bi
00에 상어가 들어감.

물고기는 번호작은 친구부터 다음과 같이 이동함.
    이동가능 : 빈칸, 다른물고기
    이동불가 : 상어
    가능할때까지 반시계 회전
    다 츄라이해봐도 안되면 이동 안함.
    이동할땐 swap함.

그 후 상어가 이동함
    한번에 여러칸 이동 가능. => 젤 큰거 먹으면 되려나?
    지나가는 칸에 있는 물고기는 안먹음.
    BLANK로는 이동 불가
    이동불가시 리턴.


# io
mtrx(n,di)
상어가 먹을 수 있는 물고기 번호의 합의 최대 리턴

# strategy
사실상 문제는.. 상어를 몇 칸 이동시켜야할지 모른다는 점이다.
각 칸을 이동시킬 떄의 결과를 매개변수로 계속해서 저장시킨다면..
answer를 글로벌로 놓고.
그렇게 하는 방법도 나쁘진 않아보인다.
나동빈 풀이에서 이렇게 했는지 함 보자.

# pseudo code



'''
from pprint import pprint

ds = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
mtrx = []
for _ in range(4):
    inp = list(map(int, input().split()))
    row = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(8):
        r, c = divmod(i, 2)
        row[r][c] = inp[i]
    mtrx.append(row)
pprint(mtrx)

```

```python
'''
# notes
mtrx 4*4
각 물고기는 번호와 방향을 가짐
번호 : 1~16 각 하나씩
방향 : 8방향

상어는 0,0 물고기 먹고 0,0에 들어감. 방향 카피.

물고기 이동:
    번호 작은것부터.
    이동가능 : 빈칸, 다른물고기 있는 칸 (swap)
    이동불가 : 경계막힘, 상어
    이동 가능할때까지 반시계 회전, 그래도 안되면 포기.
    스왑당한건 이동한걸로 안침. 정직하게 반복문 돌리면 됨.

상어 이동:
    한번에 여러 칸 이동 가능.
    역시 물고기 섭취 후 방향 카피함.
    두칸 이상 이동시 사이에 있는 물고기는 안먹음.
    BLANK로는 이동불가. 무조건 먹어야함.
    이동불가시 끝.



# io
mtrx(번호, 방향)

상어가 먹을 수 있는 물고기 번호합 최대

# strategy
상어의 이동을 재귀해야 할 것 같다. 마지막에 각 경우에 대해서 재귀하면 됨.
'''
answer = 0,0물고기번호

fish_rcs = [(-1,-1), ...]

for r in range(4):
    for c in range(4):
        fi, di = mtrx[r][c]
        fish_rcs[fi] = (r, c)

fi, di = mtrx[0][0]
mtrx[0][0] = [SHARK,방향] # 매트릭스는 좌표로 찾을 수 있도록
fish_rcs[fi] = (BLANK,BLANK) # fish_rcs는 번호로 찾는거
shr, shc, shdi = 0, 0, 방향

result = 0

def simulate(result):
    for fi in range(1, 17): # 첫 물고기부터
        r, c = fish_rcs[fi]
        if r == BLANK: # 이미 먹힌 물고기에게 조의를..
            continue
    
        for tmp_di in range(di, di+8):
            이동가능하다면:
                이동
                break
    
    shark_dist = 1
    
    while True:
        dr, dc =
        new_shr, new_shc = shr +
        if 잡아먹을수있어(new_shr, new_shc):
            fi, di = mtrx[new_shr][new_shc]
            잡아먹고 상어 옮기고 그 상태 넘겨서 재귀
    잡아먹을 수 없는 경우라면:
        결과값 더 크게 나올 수 있다면 갱신


    new
    shark_dist += 1
```