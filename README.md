# CodingTest
코테 준비용 리포지토리

## 교재
이것이 취업을 위한 코딩 테스트다 - 나동빈  

## 참고 레포
[Link](https://github.com/ndb796/python-for-coding-test)

## Python tips
- iterating through two lists in parallel : zip함수를 쓴다.
```
as = [1, 2, 3]
bs = [4, 5, 6]
for a, b in zip(as, bs):
    print(a, b)

# 근데 그냥 a_b = [(1,4), (2,5), (3,6)] 으로 선언하는 것도 방법.
```

- map함수는 문자열도 하나하나 쪼개준다. 예를들면
```
hi = '123456'
bye = list(map(int, hi)) #[1,2,3,4,5,6]
```

- 힙
  - 우선순위큐가 필요할 경우, 힙을 쓰자. 기본은 최소힙.
  - 최대힙이 필요할 경우 마이너스 붙이면 됨.
  - 시간복잡도 면에서 이득.
```
import heapq
q = []
heapq.heappush(q, (10, '우선순위high'))
heapq.heappush(q, (30, '우선순위low'))
heapq.heappush(q, (20, '우선순위mid'))

print(heapq.heappop(q)) # 우선순위high
print(heapq.heappop(q)) # 우선순위mid
print(heapq.heappop(q)) # 우선순위low
```

## 일반 tips
- 효율성 점수가 없는 문제는 구현을 하는데에 초점을 두자. 괄호변환 문제의 get_slicepoint 함수를 그렇게 구현할걸.
- 팩토리얼은 구현이고 피보나치는 DP구나