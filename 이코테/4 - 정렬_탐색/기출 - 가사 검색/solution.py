def solution(words, queries):
    answer = [0]*(len(queries))
    for query_idx in range(len(queries)):
        query = queries[query_idx]
        # print(f'쿼리 {query}를 알아보자')
        for word in words:
            if len(word) != len(query):
                # print(f'{word} 와 {query}의 길이가 다름')
                continue
            ok = True
            for i in range(len(query)):  # 각 알파벳별로 탐색
                if not (query[i] == '?' or word[i] == query[i]):
                    # print(f'{word}의 경우 {i}에서 매칭안되는거 발견')
                    ok = False
                    break
            if ok:
                # print(f'{word}의 경우 매칭됨')
                answer[query_idx] += 1

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
      "fro??", "????o", "fr???", "fro???", "pro?"]))
