'''
<io>
n : 표의 행 개수
k : 처음 인덱스
cmds : 명령어 모음

return : "OOOOXOOO"


<notes>
이동, 삭제, 복구
이동(U, D)
    카운트 n번될때까지 반복:
        삭제 안될때까지 인덱스 옮기고
        카운트 += 1
삭제(C)
    현재거 False로 만든담에 스택에 인덱스 저장
    맨 마지막 인덱스면:
        1회 위로 이동
    그게 아니면:
        1회 아래 이동 (인덱스 옮기는게 아님에 유의)

복구(Z)
    단순히 스택에서 꺼낸 인덱스 True로 만들어주면 됨.


<strategy>
세 연산에 대한 함수를 만들어주면 될것같다.
복구된건 스택에 쌓을 수있도록 하고.


'''


def cursor_in_last(pyo, idx, n):
    for last_safe_idx in range(n - 1, -1, -1):
        if pyo[last_safe_idx]:
            break


    if idx > last_safe_idx:
        return True
    return False


def solution(n, k, cmds):
    pyo = [True for _ in range(n)]
    s = []
    idx = k

    for cmd in cmds:
        '''
        이동(U, D)
            카운트 n번될때까지 반복:
                삭제 안될때까지 인덱스 옮기고
                카운트 += 1
        삭제(C)
            현재거 False로 만든담에 스택에 인덱스 저장
            맨 마지막 인덱스면 (꼭 n-1이 아니라, 남아있는 것 중 마지막이어야함.):
                1회 위로 이동
            그게 아니면:
                1회 아래 이동 (인덱스 옮기는게 아님에 유의)

        복구(Z)
            단순히 스택에서 꺼낸 인덱스 True로 만들어주면 됨.
        '''
        if cmd[0] == 'U':  # 위
            to_move = int(cmd.split()[1])
            mv_cnt = 0
            while mv_cnt < to_move:
                while True:
                    idx -= 1
                    if pyo[idx]:
                        break
                mv_cnt += 1


        elif cmd[0] == 'D':  # 아래
            to_move = int(cmd.split()[1])
            mv_cnt = 0
            while mv_cnt < to_move:
                while True:
                    idx += 1
                    if pyo[idx]:
                        break
                mv_cnt += 1

        elif cmd[0] == 'C':  # 삭제
            s.append(idx)
            pyo[idx] = False

            if cursor_in_last(pyo, idx, n):
                while True:
                    idx -= 1
                    if pyo[idx]:
                        break
            else:
                while True:
                    idx += 1
                    if pyo[idx]:
                        break
        elif cmd[0] == 'Z': # 복구
            i = s.pop()
            pyo[i] = True

    answer = []
    for not_deleted in pyo:
        if not_deleted:
            answer.append('O')
        else:
            answer.append('X')

    return ''.join(answer)