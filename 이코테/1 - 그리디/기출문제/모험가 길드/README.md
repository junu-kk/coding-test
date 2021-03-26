# 모험가 길드

## 느낀점
* 

## notes
* 공포도 x 이상인 모험가는 그룹멤버가 x명 이상이어야 함.

## input
```
5 // 모험가 5명
2 3 1 2 2 // 각 모험가의 공포도
```

## output
```
2 // 여행을 떠날 수 있는 그룹 최대는 2. -> 322 / 21
```

## strategy
* desc sort 해서 높은 공포도의 모험가를 우선으로 묶으면 되겠다.
* answer는 1, member_n은 1, member_max_n은 ppl[0]에서 출발.
* range(1, 5) 반복문 돌면서
  * member_n 2
  * member_n 3
  * member_n == member_max_n이므로
    * member_n = 0
    * answer += 1
    * member_max_n = ppl[i]
  * 쭉쭉 반복.
