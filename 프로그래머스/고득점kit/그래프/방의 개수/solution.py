from collections import defaultdict as dd

ds = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def solution(arrows):
    answer = 0
    visit_t = dd(list)
    r, c = 0, 0

    for arrow in arrows:
        # 굳이 두번 하는 이유 : 한 번 갈 걸 두번 감으로서, 딱 붙어있는 모래시계의 상황을 예방할 수 있음.
        for _ in range(2):
            dr, dc = ds[arrow]
            newr, newc = r + dr, c + dc

            # 1. 일반적인 점 재방문
            if (newr, newc) in visit_t and (r, c) not in visit_t[(newr, newc)]:
                answer += 1
                visit_t[(r, c)].append((newr, newc))
                visit_t[(newr, newc)].append((r, c))
            # 첫 방문
            elif (newr, newc) not in visit_t:
                visit_t[(r, c)].append((newr, newc))
                visit_t[(newr, newc)].append((r, c))

            # 다음 ARROW로 넘어갈 준비.
            r, c = newr, newc

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))

    # 2. 첫 방문

    # 3. 겹치는 경로

#
#
# def solution(arrows):
#     v = (0, 0)
#     vs = set()
# 로    es = []
#
#     for arrow in arrows:
#         d = ds[arrow]
#         newv = (v[0] + d[0], v[1] + d[1])
#         vs.add(newv)
#         es.append((v, newv))
#         v = newv
#
#     pprint(vs)
#     pprint(es)
#
#
# print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
