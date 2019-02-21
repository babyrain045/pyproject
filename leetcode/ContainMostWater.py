

a_list = [1,8,6,2,5,4,8,3,7]
lenth = len(a_list)
count = 0
r_index = -1
for i in a_list:
    if count < lenth/2:
        count = count + 1;
        l_flag = i
        r_flag = a_list[-count]
        r_wid = lenth
        if count == 1:
            area = (lenth - count) * i
        elif i < a_list[r_index]:
            continue
        else:
            r_wid = r_index + lenth + 1
            r_flag = a_list[r_index]
            up_area = (r_wid - count) * r_flag
            print(i,r_flag)
            print(up_area)
            if up_area > area:
                area = up_area
            r_index = r_index - 1
print(area)











