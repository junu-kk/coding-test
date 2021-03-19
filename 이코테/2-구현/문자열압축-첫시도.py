# 리스트 n개단위로 잘라 리턴
def get_sliced_list(word, n):
    sliced_list=[]
    temp=''
    i=0
    for alph in word:
        temp+=alph
        i+=1
        if i==n:
            sliced_list.append(temp)
            temp=''
            i=0
    if temp:
        sliced_list.append(temp)
    return sliced_list

#sliced list를 받아 압축한 문자열의 길이 리턴
def process(slices, n):
    new_s=''
    combo=1
    for i in range(len(slices)-1):
        if slices[i]==slices[i+1]:
            combo+=1
        else:
            if combo==1:
                new_s+=slices[i]
            else:
                new_s+=(str(combo)+slices[i])
                combo=1

    if combo==1:
        new_s+=slices[-1]
    elif combo>1 and slices[-2]==slices[-1]:
        new_s+=(str(combo)+slices[-1])
    #else:
        #new_s+=(str(combo)+slices[-2])
        #new_s+=slices[-1]
    #print(new_s)
    return len(new_s)

def solution(s):
    answer=len(s)
    for i in range(len(s)):
        new_len=process(get_sliced_list(s,i),i)
        if answer>new_len:
            answer=new_len
    return answer
