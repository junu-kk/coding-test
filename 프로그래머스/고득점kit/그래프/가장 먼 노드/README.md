## input
vn 6
vs [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


## output
1번 노드에서 가장 멀리 떨어진 노드 개수
3


## notes
양방향

## strategy
bfs를 적용한다면
depth 1..
depth 2...
...
depth n에서 끝날텐데
거기서 depth n일때의 v들 세주면 될것같다.
