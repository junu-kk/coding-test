## input && output
```
answers
[1,2,3,4,5]

return
가장 많은 문제를 맞친 사람은? (동률일시 오름차순으로)
[1]
```

## notes
```
12345 12345 ...
21 23 24 25 ...
33 11 22 44 55 ...


```

## strategy
```
상당히 쉬운 문제라고 생각됨.
그냥 1 2 3 각각 함수 만들어서 수학으로 계산 가능할듯함.
for i in range(len(answers)) 돌리는건 같을것같고..
1 : %5 == 0일때 1이면 += 1 이런식으로
2 : %2 == 1이면 ...
3 : %10일때 ...
```
