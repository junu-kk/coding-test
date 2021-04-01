# 기출 - 국영수

## 느낀점
* 리스트 쓰고 sort vs heap 쓰기 뭐가 더 효율적일까?

## notes
* 국어 desc, 영어 asc, 수학 desc, name asc

## input
```
12 // 12명
Junkyu 50 60 100 // 준규의 점수
Sangkeun 80 60 50 // ...
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
```

## output
```
Donghyuk // 정렬결과
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
```

## strategy
* 그냥 리스트 + sorted 쓰면 심심해서 heap 써봤다.
