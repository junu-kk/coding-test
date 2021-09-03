## 해설
유니온 파인드로 풀긴했는데..  
dfs면 훨 쉽게 풀렸을 것이긴 하다.  
다만 재귀에 익숙하지 않으니 이 문제 중심으로 좀 봐놓으면 좋을듯.

---

## input
```
n 컴퓨터 개수
3

computers 컴퓨터 연결정보
[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
110
110
001
```

## output
```
네트워크 개수
2
```

## notes
```
대각선 항상 1
```

## strategy
```
일단 union find가 생각난다.
1. union_vs, find_root 함수 작성하고
2. 각 엣지별로 union_vs 해준담에
3. parent_t를 root_t로 만들어주고
4. len(set(root_t))가 정답이 될거임.

근데 문제에서 주어진 건 es가 아닌 adj mtrx인데
전탐 돌리면서
r이랑 c가 다르고 set(r, c)가 안에 있지 않은 이상 add시켜주면 됨.



아직도 parent_t와 root_t가 조금 헷갈린다.
나동빈 강의 다시 함 보자.
```
