'''
문제 이해는 완료..

각각 실행하며 괜찮은가? 를 판단하면 됨.
괜찮으면 그대로 삽입or삭제. 아니면 무시.

그럼 삽입할때 괜찮은지 어떻게 판단할까?
기둥이면
    바닥위 or 보끝위 or 기둥위
    y좌표0 or (x좌표-1,y좌표-1,보) 존재 or (x좌표+1, y좌표-1, 보) 존재 or (x좌표,y좌표-1,기둥) 존재
보면
    한쪽끝기둥위 or 양쪽끝보연결
    (x, y-1, 기둥) or (x+1, y-1, 기둥) or ((x-1, y, 보) and (x+1, y, 보))
    
그럼 삭제할땐 어떻게 판단할까?
기둥이면
    (x, y)와 (x, y+1)값 가진 모든 기둥&보에 대해 체크
보면
    (x, y)와 (x+1, y)값 가진 모든 기둥&보에 대해 체크
'''

GIDUNG = 0
BO = 1

def gidung_create_test(x,y, frame):
    if y == 0 or [x-1, y, 1] in frame or [x+1, y, 1] in frame or [x, y-1, 0] in frame:
        return True
    return False

def bo_create_test(x,y, frame):
    if [x,y-1,0] in frame or [x+1,y-1,0] in frame or ([x-1,y,1] in frame and [x+1,y,1] in frame):
        return True
    else:
        return False

def gidung_delete_test(x,y,frame):
    for each in frame:
        if each[0] == x and each[1] == y and each[2] == GIDUNG:
            if not gidung_create_test(each[0],each[1],frame):
                return False
        if each[0] == x and each[1] == y and each[2] == BO:
            if not bo_create_test(each[0],each[1],frame):
                return False
        if each[0] == x and each[1] == y+1 and each[2] == GIDUNG:
            if not gidung_create_test(each[0],each[1],frame):
                return False
        if each[0] == x and each[1] == y+1 and each[2] == BO:
            if not bo_create_test(each[0],each[1],frame):
                return False
    return True
def bo_delete_test(x,y,frame):
    for each in frame:
        if each[0] == x and each[1] == y and each[2] == GIDUNG:
            if not gidung_create_test(each[0],each[1],frame):
                return False
        if each[0] == x and each[1] == y and each[2] == BO:
            if not bo_create_test(each[0],each[1],frame):
                return False
        if each[0] == x+1 and each[1] == y and each[2] == GIDUNG:
            if not gidung_create_test(each[0],each[1],frame):
                return False
        if each[0] == x+1 and each[1] == y and each[2] == BO:
            if not bo_create_test(each[0],each[1],frame):
                return False
    return True
        

    
def solution(n, build_frame):
    frame = []
    for each in build_frame:
        if each[2] == GIDUNG and each[3] == 1:
            if gidung_create_test(each[0], each[1], frame):
                frame.append([each[0], each[1], GIDUNG])
                print(1)
            else:
                print(2)
        elif each[2] == BO and each[3] == 1:
            if bo_create_test(each[0], each[1], frame):
                frame.append([each[0], each[1], BO])
                print(3)
            else:
                print(4)
        elif each[2] == GIDUNG and each[3] == 0:
            if gidung_delete_test(each[0], each[1], frame):
                frame.remove([each[0],each[1],GIDUNG])
                print(5)
            else:
                print(6)
        elif each[2] == BO and each[3] == 0:
            if bo_delete_test(each[0], each[1], frame):
                frame.remove([each[0], each[1], BO])
                print(7)
            else:
                print(8)

    
    return sorted(frame)


#print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))