
strg = ''
inpt = input().split()
rest = zip(*inpt)
for i in rest:
    b = set(i)
    if len(b) == 1:
        strg = strg + i[0]
    else:
        break
print(strg)
