import json
from collections import defaultdict as dd

d1_bil = dd(int)
d1_ban = dd(int)
d2_bil = dd(int)
d2_ban = dd(int)
d3_bil = dd(int)
d3_ban = dd(int)

with open('1.json') as j:
    d = json.load(j)
    for t in d:
        for each in d[t]:
            bil_loc, ban_loc, bil_dur = each
            if int(t) < 240:
                d1_bil[bil_loc] += 1
                d1_ban[ban_loc] += 1
            elif int(t) < 480:
                d2_bil[bil_loc] += 1
                d2_ban[ban_loc] += 1
            else:
                d3_bil[bil_loc] += 1
                d3_ban[ban_loc] += 1

print(sorted(d1_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d2_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d3_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))

print()
print()
d1_bil = dd(int)
d1_ban = dd(int)
d2_bil = dd(int)
d2_ban = dd(int)
d3_bil = dd(int)
d3_ban = dd(int)

with open('2.json') as j:
    d = json.load(j)
    for t in d:
        for each in d[t]:
            bil_loc, ban_loc, bil_dur = each
            if int(t) < 240:
                d1_bil[bil_loc] += 1
                d1_ban[ban_loc] += 1
            elif int(t) < 480:
                d2_bil[bil_loc] += 1
                d2_ban[ban_loc] += 1
            else:
                d3_bil[bil_loc] += 1
                d3_ban[ban_loc] += 1

print(sorted(d1_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d2_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d3_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))

print()
print()
d1_bil = dd(int)
d1_ban = dd(int)
d2_bil = dd(int)
d2_ban = dd(int)
d3_bil = dd(int)
d3_ban = dd(int)

with open('3.json') as j:
    d = json.load(j)
    for t in d:
        for each in d[t]:
            bil_loc, ban_loc, bil_dur = each
            if int(t) < 240:
                d1_bil[bil_loc] += 1
                d1_ban[ban_loc] += 1
            elif int(t) < 480:
                d2_bil[bil_loc] += 1
                d2_ban[ban_loc] += 1
            else:
                d3_bil[bil_loc] += 1
                d3_ban[ban_loc] += 1

print(sorted(d1_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d2_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d3_bil.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))
print(sorted(d1_ban.items(), key=lambda x: x[1], reverse=True))

print()
print()
