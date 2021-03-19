# 나동빈

'''
1. rotate함수 요긴하게 쓰일듯
2. 완탐을 써도 되겠다 판단되면 인정사정없이 메모리 쓰고 포문 돌리고 하자.
'''

# 열쇠체크
def check(newLock):
    lock_l = len(newLock) // 3
    for i in range(lock_l, lock_l * 2):
        for j in range(lock_l, lock_l * 2):
            if newLock[i][j] != 1: # 하나라도 아다리가 안맞으면 false
                return False
    return True # 모두 맞으면 True


# 돌리기 -> 
def rotate(a):
    r = len(a)
    c = len(a[0])
    # 돌렸으니까 거꾸로!
    rotated = [[0] * r for _ in range(c)]
    
    for i in range(r):
        for j in range(c):
            # row는 당연히 돌렸으니까 j일거고
            # column은 오른쪽부터 가야하니까.. r-1부터 0까지 가야하니까 r-1-i라고 할 수 있지..
            # -i라고 해도 되지 않나?? -> -i로 하면 절반 실패 뜬다.
            rotated[j][r-1-i] = a[i][j]
    
    return rotated


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    bigLock = [[2]*lock_size*3 for _ in range(lock_size*3)]
    
    for i in range(lock_size):
        for j in range(lock_size):
            bigLock[lock_size+i][lock_size+j] = lock[i][j]
    
    # 4방향 돌리기 반복
    for _ in range(4):
        # 돌리고
        key = rotate(key)
        # 자물쇠 두배 크기만큼 (모든 공간을 활용해)
        for x in range(lock_size*2):
            for y in range(lock_size*2):
                # 키를 끼워보고
                for i in range(key_size):
                    for j in range(key_size):
                        bigLock[x+i][y+j] += key[i][j]
                # 확인 한번이라도 되면 리턴트루 끝
                if check(bigLock):
                    return True
                # 원상복구
                for i in range(key_size):
                    for j in range(key_size):
                        bigLock[x+i][y+j] -= key[i][j]
    return False