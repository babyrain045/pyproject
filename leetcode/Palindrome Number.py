
x = 122
x = list(str(x))
y = list(x)     #这里的赋值  不应该直接使用'='，而应该复制一个新的list

for i in x:
    a = y.pop()
    if i == a:
        if y == []:
            print(True)
        continue
    else:
        print(False)
        break;

# 该方法请求了新的内存来存储列表，因此内存占用较高，可以考虑内存消耗更小的方法