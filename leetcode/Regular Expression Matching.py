import re


s = 'aa'
p = 'a*'
rlts = re.match(p, s)
print(rlts)
if rlts is None:
    print(False)
else:
    rlts_letr = rlts.group()
    if rlts_letr == s:
        print(True)
    else:
        print(False)