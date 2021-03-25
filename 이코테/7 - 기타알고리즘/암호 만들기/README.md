# 암호 만들기

## 느낀점
* 

## notes
* 암호는 4개의 알파벳 소문자로 구서오디며, 최소 한개의 모음과 최소 두 개의 자음으로 구성되어 있음.

## input
```
4 6 // 4개의 알파벳들로 구성된 암호. 문자 6개.
a t c i s w // 후보문자 6개
```

## output
```
acis // 모음 한개이상, 자음 두개이상으로 자모 짜맞춰서 asc순으로 출력.
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
```

## strategy
* 일단 4개 컴비네이션으로 뽑아서 자음두개 모음한개 통과한 것들만 퍼뮤테이션 돌리면 될듯. -> 무조건 abc순이라서 combination으로 해도 무방.
