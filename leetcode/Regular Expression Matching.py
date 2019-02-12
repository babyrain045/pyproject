
import re
a = 'ancdefgfff'
p = 'f*'

pattern = re.compile(p)
rlts = re.search(pattern, a).group()
print(rlts)