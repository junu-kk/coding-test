## 해설
[참조 블로그](https://velog.io/@narastro/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%A9%EC%9D%98-%EA%B0%9C%EC%88%98-Python)  
방문했던 정점을 재방문하는 경우 + 인접한 네 개에서의 모래시계의 경우.  
+ 왔다갔다 처리

그리고 그래프 문제에서 DefaultDICT가 많이 쓰이던데,
찾아보니까 그냥 기본자료형 정의된 딕셔너리임.

솔직히 문제에서 이거 생각할 시간 없을것같다.
이런 비슷한 문제가 나오면 제끼자.


---
## input
arrows [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]


## output
3 (방 개수)

## notes
방향은
7 0 1
6   2
5 4 3

## strategy
정점이 기준이 되는 그래프는 얼마든 만들 수 있다.  
하지만 간선이 기준이 되는 그래프는 어떻게 만들지 모르겠다.  
음.. 각 정점을 좌표로 찍고 (0, -1)
간선을 ((0,0), (0,-1))
위와 같이 나타낼 수 있긴 함.

핵심은 그래서 닫힌 도형이 몇개인지를 어떻게 판별할것인가가 문제임.
