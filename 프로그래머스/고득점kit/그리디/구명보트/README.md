## 해설
[블로그](https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-in-python)  
생각못한 투포인터 문제다.  
아이디어 한 절반은 맞았지만, 더욱 분발해야겠다.  
그리고 반복문에서 while문도 가끔 쓰일 때가 있으니, 너무 for문만 고집하지 말자.
---


## input && output
```
people
[70,50,80,50]

limit
100

return
구명보트 왔다갔다 최소 횟수
3
```

## notes
```
언제나 구출 가능한 상태.
```

## strategy
```
최소로 타야 한다.
1. 정렬을 한 담에
2. limit - person보다 작지만 최대의 사람을 태운다.
반복한다.

자료구조는 어떤 게 좋을까?
counter
list

```
