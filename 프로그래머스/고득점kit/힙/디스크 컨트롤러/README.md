## 해설
[블로그](https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99)  
작업의 소요시간 기준으로 힙이 만들어져야 한다.  
소요시간이 적은걸 먼저해야 뒤의 작업들이 덜 기다릴 것이기 때문.
계속해서 t를 올려가는게 아닌, 다음과 같이 이루어져야 할 것이다.

포인트는 SJF 방식이 가장 효율적이라는 것을 알아야 한다.  
자세한건 직접 코드를 보며 익혀보자.  
하 이문제 라인이었나 네이버였나 비슷한거 나왔어서 파야할 문제이다.  


### 힙에 넣는 조건
prev_job_start_time < 현재 시점에서 처리가능한 작업 <=현재시각
당연히 미리 들어와있어야 하고, 마지막으로 수행시작한 작업보단 나중에 들어와있어야 함.


---


## input && output
```
jobs # 0초에 들어온 3초짜리 작업, ...
[[0,3],[1,9],[2,6]]

return # 세 작업의 요청~작업종료 시간의 평균 (소수점 버림)
9
```

## notes
```
대기시간을 최소화하는 방향으로 가야 한다.
```

## strategy
```
힙을 쓰면 이게 된다?
음...
잘 모르겠으니 풀이를 보자.
```
