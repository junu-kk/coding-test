# 크롤러
- 토큰 받고
- 5개의 url을 받아서
- 이미지를 가져와 특정값 추출해 서버에 저장/삭제

[공식해설](https://tech.kakao.com/2017/10/24/kakao-blind-recruitment-round-2-2/)

## 전략
### 평가 메트릭 분석
- 정상 저장된 이미지 수 (+1.0)
- 노출돼야 하는데 노출안된 이미지 수 (-0.8)
- 노출되면 안되는데 노출된 이미지 수 (-1.2)
- 잘못된 데이터 수 (-3.0)
- 총 쿼리양 (-0.01)

### 병렬처리
- 싱글 스레드로는 초당요청제한 50건을 채우지 못할수도 있음
- 멀티프로세스 or 멀티스레드 사용 권장

### 예외처리
- api에 특정 확률로 실패하는 로직을 넣어놓음.
- 재시도 예외처리를 넣는다면 고득점에 가까워질것

### 다양한 시나리오 대응
- 이미 추가한 이미지인지 확인 : 메모리 캐시 도입
- 5개 카테고리를 다 하지 않을수도 있음

## 합격선
- 병렬처리 없이 예외&배치 처리만 해도 통과.