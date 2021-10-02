# coding-test
코테 준비용 리포지토리

## 이번주까진..
- [ ] 이코테 복습
- [ ] 바킹독 복습
- [ ] 기출 복습


## 유용한 코드모음
* [2d 리스트에서 칼럼 뽑아내기](https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array)
```py
c = [row[idx] for row in mtrx] # idx에 칼럼인덱스 넣어주면 됨
```

* [2d 리스트 회전하기](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/Miscellaneous/rotate_a_matrix_by_90_degree.py)
```py
def rotate_mtrx(mtrx):
    rl = len(a)
    cl = len(a[0])

    new_mtrx = [[0] * rl for _ in range(cl)]
    for r in range(rl):
        for c in range(cl):
            new_mtrx[c][rl - 1 - r] = mtrx[r][c]

    return res
```


* 정렬된 리스트에서 l 이상 r 이하 값 개수 뽑아내기 (O(logN))
```py
from bisect import bisect_left as bl, bisect_right as br

def count_by_range(arr, l, r):
    ri = br(arr, rv)
    li = bl(arr, lv)
    return ri-li
```