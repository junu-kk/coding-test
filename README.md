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
