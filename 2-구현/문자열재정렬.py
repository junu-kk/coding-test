s=input()
sutja=0
munja=''
for i in s:
    if i.isupper():
        munja+=i
    else:
        sutja += int(i)

print(''.join(sorted(munja))+str(sutja))