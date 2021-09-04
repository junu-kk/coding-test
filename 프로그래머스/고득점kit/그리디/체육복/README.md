## input && output
```
n
5

lost
[2,4]

reserve
[1,3,5]

return
쉅들을 수 있는 최댓값
5
```

## notes
```
바로 앞이나 뒤에게만 체육복 대여 가능
lost랑 reserve 겹칠수있음.
```

## strategy
```
set으로 바꾸는게 좋아보임.
lost_set
reserve_set으로 해주고

1. 각 reserve마다 겹치는 lost 있으면 빼주기 처리
2. 각 reserve마다
  reserve-1이 lost에 있으면 빼주고
  reserve+1이 lost에 있으면 빼준다.
3. len(reserve_set) 리턴

음 근데 set changed size during iteration 떴네
이번 들어 웰케 set을 많이 쓰는진 모르겠는데 확실히 시간복잡도 면에서 이득인것같긴 하다. 10분컷 굳.
```
