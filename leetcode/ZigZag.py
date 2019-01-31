

letter_string = 'ABCDEFG'
letter_list = list(letter_string)
print(letter_list)
num_rows = 1
count_line = 1
count_row = 1
flag = 0
line_num = []
row_num = []
for i in letter_list:
    if num_rows == 1:
        line_num.append(count_line)
        row_num.append(count_row)
        count_row = count_row + 1
    elif count_line < num_rows and flag == 0 :
        row_num.append(count_row)
        line_num.append(count_line)
        count_line = count_line + 1
    else:
        if count_line == 1:
            line_num.append(count_line)
            row_num.append(count_row)
            count_line = count_line + 1
            flag = 0
        else:
            flag = 1
            line_num.append(count_line)
            row_num.append(count_row)
            count_row = count_row + 1
            count_line = count_line - 1


print(line_num)
print(row_num)
label = list(zip(letter_list, line_num, row_num))
print(label)


results = sorted(label, key=lambda x:[x[1]])

letter_sort = [x[0] for x in results]
outstr = "".join(letter_sort)
print(outstr)


