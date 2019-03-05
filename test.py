
while True:
    try:
        stu_ope_list = input().split()
        stu_cout = int(stu_ope_list[0])
        ope_cout = int(stu_ope_list[1])
        stu_num = input().split()
        stu_list = []
        count = 0
        for i in stu_num:
            stu_list.append(int(i))
        while count <= ope_cout:
            count = count + 1
            judge_wd,ope_index,ope_val = input().split()
            ope_index = int(ope_index)
            ope_val = int(ope_val)
            if judge_wd == 'Q':
                start = min(ope_index-1,ope_val)
                end = max(ope_index-1,ope_val)
                stu_ran = stu_list[start : end]
                print(max(stu_ran))
            elif judge_wd == 'U':
                stu_list[ope_index-1] = ope_val
    except:
        break



