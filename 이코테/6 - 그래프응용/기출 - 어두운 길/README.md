# 기출 - 어두운 길
[전력난](https://www.acmicpc.net/problem/6497) 문제로 갈음.  

## 느낀점
* 

## notes
* 양방향
* 

## input
```
7 11 // vn, en
0 1 7 // 0~1, cost 7 
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
0 0 // vn, en (만약 0 0이면 종료)
```

## output
```
51 // 절약가능 최대액수
```

## strategy
* 크루스칼로 mst cost 구해서 원래 cost 합에서 빼주면 되겠다.
