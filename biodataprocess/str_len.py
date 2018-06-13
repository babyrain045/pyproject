a = 'bbbbbbbbbbbbbbb'
str_ = []
lenth = 0
for i in a:
    if i not in str_:
        str_.append(i)
    else:
        str_ = str_[str_.index(i)+1:]
        str_.append(i)
    lenth_update = len(str_)
    if lenth_update > lenth:
        lenth = lenth_update
print(lenth)


