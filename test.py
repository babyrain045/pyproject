import sys
count = 0
for line in sys.stdin:
    count = count + 1
    if count == 1:
        stu_cout, ope_cout = line.strip('\n').split()
        stu_cout = int(stu_cout)
        ope_cout = int(ope_cout)
    elif count == 2:
        stu_num = line.strip('\n').split()
        stu_list = []
        for i in stu_num:
            stu_list.append(int(i))
        print(stu_list)
    else:
        judge_wd,ope_index,ope_val = line.split()
        ope_index = int(ope_index)
        ope_val = int(ope_val)
        if judge_wd == 'Q':
            stu_ran = stu_list[ope_index-1 : ope_val]
            print(max(stu_ran))
        elif judge_wd == 'U':
            stu_list[ope_index-1] = ope_val


