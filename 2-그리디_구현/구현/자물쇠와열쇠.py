'''
열쇠 돌려서 문에 끼워넣는 그거인듯.
당연히 key는 lock의 사이즈 이하이고

lock의 0 부분이 key의 1 부분과 맞아야 하며, lock의 1은 key의 0이어야 한다.
lock의 바깥을 2라고 했을때, lock의 2는 key의 어느 부분이 와도 상관없다.
bigLock 놓고, key 돌려가면서 완탐 고고


'''


def solution(key, lock):
    k = len(key)
    l = len(lock)
    bigLock = [[2]*l*3 for _ in range(l*3)]

    for i in range(l):
        for j in range(l):
            bigLock[l+i][l+j] = lock[i][j]
    print(bigLock)

    # 2차원을 돌리는건 짤 수 있는데
    # 어떻게 조금씩 움직이지??

    answer = True
    return answer
