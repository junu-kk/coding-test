# 현재 풀이
'''
길이가 n이면 n//2까지만 인덱스 돌려도 되겠다.
aabbaccc : 2a2ba3c
ababcdcdababcdcd : 2ab2cd2ab2cd 2ababcdcd
abcabcdede : 2abcdede abcabc2de
xababcdcdababcdcd : xababcdcdababcdcd

그리디하게 가볼까?
answer = len(s)로 잡아놓고
1반복 : 1칸씩 슈루룩 살펴보며 겹칠때마다 -1씩
2반복 : 2칸씩 슈룩 슈룩 살펴보며 겹칠때마다 -2씩 
3반복 : 

'''


def solution(s):
    real_answer = len(s)
    for cut_danwi in range(1, len(s)//2 + 1):
        # 17자의 경우, 1~8자까지 자르기 시도 ㄲ.
        answer = len(s)
        temp_s = ''
        count = 0
        repeats = 0
        repeat_s = ''

        for i in range(len(s)):  # 첨 이후 문자열 하나하나 뜯어보기 시작
            if count < cut_danwi:  # 쿨타임이 찰때까지 temp_s를 모음
                temp_s += s[i]
                count += 1
                continue

            # 자 이제 쿨타임이 찼어요
            print(temp_s, end=' : ')
            if repeats == 0:  # 1. 반복하지 않던 상황이면 반복 시작
                repeats += 1
                repeat_s = temp_s
                count = 0
                temp_s = ''
                print(1)

            elif temp_s == repeat_s:  # 2. 반복하던 상황인데 딱 맞네!
                repeats += 1
                answer -= cut_danwi
                count = 0
                temp_s = ''
                print(2)

            else:  # 3. 반복이 깨진 상황
                repeats = 0
                repeat_s = ''
                count = 1
                temp_s = s[i]
                print(3)

        if answer < real_answer:
            real_answer = answer
    return real_answer


# 여기서부턴 옛날의 풀이
'''
    n은 1부터 len(s)//2까지 ㄱㄱ
    aabbaccc
        n==1 : 2a2ba3c
    ababcdcdababcdcd
        n==2 : 2ab2cd2ab2cd
        n==8 : 2ababcdcd
    abcabcdede
        n==3 : 2abcdede
    abcabcabcabcdededededede
    xababcdcdababcdcd
    
    '앞에서부터 자른다'
    1. n만큼 잘라서 새로운 리스트에 저장
    2. i번째 i+1번째 비교해서
        같으면 continue
        다르면 새 문자열에 대입
        
    예시를 들어보자.
    [a a b b a c c c]
        a a 같네? combo+=1
        a b 다르네? new_s+='2a'
        b b 같네? combo+=1
        b a 다르네? new_s+='2b'
        a c 다르네? new_s+='a'
        c c 같네? combo+=1
        c c 같네? combo+=1
        후속처리(3c를 넣어야..)
            콤보존재x
            if combo==1:
                new_s+=slices[-1]
            콤보존재, 막콤보
            elif combo>1 and slices[-2]==slices[-1]:
                combo+=1
                new_s+=(str(combo)+slices[i])
            콤보존재, 막콤보x
            else:
                콤보처리
                new_s+=(str(combo)+slices[-2])
                new_s+=slices[-1]
    [abc abc ded e]
        abc abc 같네? combo+=1
        abc ded 다르네? new_s+='2abc'
        ded e 다르네? new_s+='ded'
        후속처리(e를 넣어야.)
'''

# #리스트 n개단위로 잘라 리턴
# def get_sliced_list(word, n):
#     sliced_list=[]
#     temp=''
#     i=0
#     for alph in word:
#         temp+=alph
#         i+=1
#         if i==n:
#             sliced_list.append(temp)
#             temp=''
#             i=0
#     if temp:
#         sliced_list.append(temp)
#     return sliced_list

# #sliced list를 받아 압축한 문자열의 길이 리턴
# def process(slices, n):
#     new_s=''
#     combo=1
#     for i in range(len(slices)-1):
#         if slices[i]==slices[i+1]:
#             combo+=1
#         else:
#             if combo==1:
#                 new_s+=slices[i]
#             else:
#                 new_s+=(str(combo)+slices[i])
#                 combo=1

#     if combo==1:
#         new_s+=slices[-1]
#     elif combo>1 and slices[-2]==slices[-1]:
#         new_s+=(str(combo)+slices[-1])
#     #else:
#         #new_s+=(str(combo)+slices[-2])
#         #new_s+=slices[-1]
#     #print(new_s)
#     return len(new_s)

# def solution(s):
#     answer=len(s)
#     for i in range(len(s)):
#         new_len=process(get_sliced_list(s,i),i)
#         if answer>new_len:
#             answer=new_len
#     return answer
