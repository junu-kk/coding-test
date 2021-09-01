## 해설
[참고 블로그](https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84-Floyd-Warshall-Level3)  
놓친점 : 위상정렬을 처음에 생각했었으나, 플로이드워셜의 아이디어를 떠올리면 되는 문제였다.    
순위라는 건 결국 자기자신을 제외한 모든 점들과 순위가 나온다면 되는 문제이므로 그렇다.
None, True, False를 적절히 활용해야 함.  
플로이드와샬 또한 COST가 아닌 NTF를 저장한다면 이런 식으로 응용할 수 있겠군.  


---

## input
```
vn 5
en [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
```

## output
정확한 순위를 매길 수 있는 선수의 수
```
2
```

## notes
단방향 그래프로 나타낼 수 있을듯.


## strategy
inbound와 outbound가 중요할 것 같은 느낌이..
그 마지막 장에 그 알고리즘.. 위상정렬!
근데 어케하는지 까먹음. 다시 복습해야할듯.