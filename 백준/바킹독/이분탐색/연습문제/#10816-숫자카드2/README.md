## bl, br의 원리
내부 소스코드를 뜯어보면 다음과 같다.
```python
def bisect_left(a, x): # 가장 작은 인덱스를 찾아야 하므로
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1 # 명백하게 값이 클때만 lo를 갱신해주고
        else: hi = mid # 그 외엔 hi를 갱신해준다.
    return lo
```
```python
def bisect_right(a, x): # 가장 큰 인덱스를 찾아야 하므로 
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid # 명백하게 값이 작을때만 hi를 갱신해주고
        else: lo = mid+1 # 그 외엔 lo를 갱신해준다.
    return lo
```

