
while True:
    try:
        stu_ope_list = input().split()
        stu_cout = int(stu_ope_list[0])
        ope_cout = int(stu_ope_list[1])
        stu_num = input().split()
        stu_list = []
        show_list = []
        for i in stu_num:
            stu_list.append(int(i))
        while ope_cout > 0:
            ope_cout = ope_cout - 1
            judge_wd,ope_index,ope_val = input().split()
            ope_index = int(ope_index)
            ope_val = int(ope_val)
            if judge_wd == 'Q':
                start = min(ope_index,ope_val)
                end = max(ope_index,ope_val)
                stu_ran = stu_list[start-1 : end]
                show_list.append(max(stu_ran))
            elif judge_wd == 'U':
                stu_list[ope_index-1] = ope_val
            else:
                break
        for i in show_list:
            print(i)
    except:
        break


