# 기출 - 문자열 압축

## 느낀점
* 디버깅 하면서 알아낸 부분 : 문자가 열번 넘게 반복될때, 문자열 길이도 하나 늘어날 것이다. 난 한자리수만 생각했었음 (답 안보고 알아냈다 아싸~)
* 아침에 문제를 풀 때 컨디션을 좋게 해야겠다. 이거 풀 때 약간 상쾌하지 않고 약간 잠긴 느낌이어서 조금 아쉬웠다. 특히 시뮬레이션 문제는 머리가 쌩쌩 돌아갈 때 푸는게 좋을것같다.
* divmod 함수의 재발견

## notes
* 일단 처음에 자르고 압축을 하는 형태.
* s_l은 1~1000

## params
```
aabbaccc // 단위 1, 2a2ba3c
```
```
ababcdcd / ababcdcd // 단위 8
```
```
abc / abc / ded / e // 단위 3
```
```
abcabcabcabcdededededede // 단위 6
```
```
xababcdcdababcdcd // x2ab2cd2ab2cd 안됨? -> 일단 자르고 붙이는 것이기에 안됨.
```

## return
```
7 // 총 길이
```
```
9
```
```
8
```
```
14
```
```
17
```

## strategy
```
단위2 : ab / ca / bc/ ab/ ca/ bc/ de/ de/ de/ de/ de/ de -> abcabcabcabc6de
단위3 : abc/abc/abc/abc/ded/ede/ded/ede -> 4abcdededededede
단위4 : abca/bcab/cabc/dede/dede/dede -> abcabcabcabc3dede
단위6 : abcabc/abcabc/dedede/dedede -> 2abcabc2dedede
```
* 자르는 건 문자열 길이의 절반까지 시도해보면 된다.
* 원래 길이를 일단 정답으로 두고, 잘라가면서 더 작은 값이 나오면 대입해주면 됨.
* 어떻게 자를 것이냐?
  * 그냥 반복문으로 돌리는 거지 뭐.
  * 다만 실제로 문자를 append하기보단, 수학으로 할 수 있을것같다.
  * 마지막 잉여 직전까지 반복문 돌려주고, 잉여는 그냥 순수히 더하면 됨.


* 길이 9를 자른다고 생각해보자.
  * cut_l은 2~4로 돌릴 것이고
  * 2일땐 반복을 4번, 3일땐 반복을 3번, 4일땐 반복을 2번 해야함.
  * s_l // cut_l 하면 반복횟수가 나오는 셈.
  * 반복이 2회 될 떄부터 이득이 생김.


```
aabbaccc
```
```
ababcdcdababcdcd // 단위 8
```
```
abcabcdede // 단위 3
```
```
abcabcabcabcdededededede // 단위 6
```
```
xababcdcdababcdcd // x2ab2cd2ab2cd 안됨? -> 일단 자르고 붙이는 것이기에 안됨.
```