

a_list = [1,8,6,2,5,4,8,3,7]
lenth = len(a_list)
count = 1
r_index = -1
r_flag = a_list[r_index]
area = 0
while(count - r_index <= lenth):
        if a_list[count-1] < a_list[r_index]:
            print(a_list[count-1],a_list[r_index])
            r_wid = lenth + r_index + 1
            up_area = (r_wid - count) * a_list[count-1]
            if up_area > area:
                area = up_area
            count = count + 1
            print("jishu:",count)
            print(a_list[count-1],r_flag)
            print("zuobian area:",up_area,a_list[count - 1],r_wid,count)
        else:
            r_wid = r_index + lenth + 1
            r_flag = a_list[r_index]
            up_area = (r_wid - count) * r_flag
            print(a_list[count-1],r_flag)
            print("youbian area:",up_area)
            if up_area > area:
                area = up_area
            r_index = r_index - 1

print(area)











