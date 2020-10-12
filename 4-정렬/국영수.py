n=int(input())
name_guk_yeong_su = []
for i in range(n):
    name, guk, yeong, su = input().split()
    name_guk_yeong_su.append((-int(guk), int(yeong), -int(su), name))

for _, __, ___, name in sorted(name_guk_yeong_su):
    print(name)