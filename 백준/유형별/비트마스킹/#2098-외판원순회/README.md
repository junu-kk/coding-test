## 비트연산 정리

- `1 << n` : n번째 비트를 켠다. (2^n과 동일)
- `1 << n - 1` : n개의 비트를 모두 켠다.
- 유용한 트릭들
    - 2^n 여부 확인하기 : `n & (n-1) == 0`
    - 이진수 형태일 때 1비트의 개수 구하기
      - 계속 2로 나눠가면서 나머지가 있을때마다 1씩 늘려준다.
- `1 << n`으로 할 수 있는 다양한 연산들
  - 원소 추가 : |
  - 원소 제거 : & ~
  - 원소 조회 : &
  - 원소 토글 : ^

```python
def count_bit(n):
    return n % 2 + count_bit(n // 2) if n >= 2 else n

```
- 집합론과 비트의 만남
  - 2진수의 집합 표현
    - 2진수 n을 집합으로 어떻게 표현할까?
    - 2진수에서 켜져있는 자리를 원소로 표현하면 된다.
    - 그러면 210 == 10010010 == {1,4,6,7}이 되겠지.
  - b번째 비트 끄기
    - a-b는 곧 a교b여이다. 
    - `turn_off(a, b)`는 곧 `a & ~(1 << b)`

## bf로 풀기
- 각 도시에서 출발해 다른 모든 도시를 차례로 방문하는걸 싹 다 구한다음에 그 최소를 리턴
- 시간복잡도 나가리되기 딱 좋은 풀이

## DP로 풀기
```python

```

