pre = [0]*(ord('z')-ord('a')+1)
post = [0]*(ord('z')-ord('a')+1)

pre_string = input()
post_string = input()

for alph in pre_string:
    idx = ord(alph)-ord('a')+1
    pre[idx] += 1

for alph in post_string:
    idx = ord(alph)-ord('a')+1
    post[idx] += 1

common_n = 0
for pre_post_alph_n in zip(pre, post):
    common_n += min(pre_post_alph_n)

print(max(len(pre_string), len(post_string)) - common_n)
