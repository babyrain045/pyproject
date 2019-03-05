


while True:
    try:
        rand_num = int(input())
        num_list = []
        cout = 0
        while cout < rand_num:
            cout = cout + 1
            a = int(input())
            if a not in num_list:
                num_list.append(a)
        num_list_order = sorted(num_list)
        for i in num_list_order:
            print(i)
    except:
        break