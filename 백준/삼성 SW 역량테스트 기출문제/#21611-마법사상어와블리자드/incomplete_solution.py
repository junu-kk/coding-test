# '''
# 삥글뺑글 + 폭파 유형 (둘 다 내가 취약한 유형)
# https://imksh.com/64 보도록 하자.
#
# # notes
# 가운데부터 반시계 빙글뱅글
# 네 개 이상 연속하는 구슬이 있을때 폭-발, 이는 계속해서 일어남. => 폭발문제..!
# 그리고 각각 그룹지어서 (개수, 번호)로 바뀜. 다 담지 못하는 경우 사라짐.
# 폭발한 1번 + 2*폭발한 2번 + 3*폭발한 3번
#
# # io
# n cmd_n
# mtrx
# cmds (방향, power)
#
# # strategy
# 1 1 2 2 3 3 ...
# 일단 n번째 r, c를 구하는 함수 내지는 리스트를 짜야 할 것 같음. n*n-1까지 받을 수 있겠지.
#
# 1. 슈팅
# 2. 네개연속 폭발 반복
# 3. 구슬 그룹지어 변화
#
# mtrx와 일렬리스트를 잘 와리가리해야할것같다. 정확히 말하면
# 슈팅땐 mtrx에서 처리하고
# 그걸 일렬리스트에 담은 다음에
# 폭발과 변화를 처리하고
# 그걸 다시 mtrx로 옮기는 걸 반복하면 되겠다.
# # pseudo code
#
#
#
# '''
# ds = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
# loc_ds = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 왼 아 오 위
# n, cmd_n = map(int, input().split())
# cen = (n - 1) // 2
# tmp = (cen, cen)
# locs = [tmp] * (n * n)  # 인덱스는 순서요 값은 rc로다
# di = 0
# count = 2
# i = 1
# while True:
#     try:
#         dr, dc = loc_ds[di]
#         r, c = locs[i - 1]
#         it_n = count // 2
#         for _ in range(it_n):
#             r += dr
#             c += dc
#             locs[i] = (r, c)
#             print(locs[i])
#             i += 1
#         count += 1
#         di = di + 1 if di < 3 else 0
#     except IndexError:
#         break
#
#
# '''
# 슈팅땐 mtrx에서 처리하고
# 그걸 일렬리스트에 담은 다음에
# 폭발과 변화를 처리하고
# 그걸 다시 mtrx로 옮기는 걸 반복하면 되겠다.
# '''
# mtrx = [map(int, input().split()) for _ in range(n)]
# for _ in range(cmd_n):
#     di, power = map(int, input().split())
#     dr, dc = ds[di]
#     r, c = cen+dr, cen+dc
#     for _ in range(power):
#         mtrx[r][c] = -1
#         r += dr
#         c += dc
#     beads = []
#     for r, c in locs[1:]:
#         if mtrx[r][c] == -1:
#             continue
#         if mtrx[r][c] == 0:
#             break
#         beads.append(mtrx[r][c])
#
#     new_beads = []
#     while True:
#         for i in range(len(beads)):
#             # 여기서 폭발 처리
#
#     # 변화 처리
#
#     # mtrx 변환 처리
#
#
