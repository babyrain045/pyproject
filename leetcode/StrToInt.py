

s = " ---12 "

import re
flag = 1
minus = 1

pattern = re.compile(r"\s*[+-]?[0-9]+")
reslt = re.match(pattern, s)
if reslt is not None:
    str = int(reslt.group())
    if str < 0:
        flag = -1
        minus = 0
    if abs(str) < 2**31:
        print(str*flag)
    else:
        print(str*flag - minus)