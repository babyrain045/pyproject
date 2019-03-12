import sys
import collections
error_dict = collections.OrderedDict()
while True:
    try:

        file_input = input().split('\\')[-1]
        file_path, error_line = file_input.split()[0][-16:], file_input.split()[1]
        error_path = file_path + '_' + error_line

        if error_path in error_dict:
            error_dict[error_path] = error_dict[error_path] + 1
        else:
            error_dict[error_path] = 1
        itm = error_dict.items()
        itm = sorted(itm, key=lambda k: k[1], reverse=True)






    except:
        break
for i in range(0,min(len(itm),8)):
    file_name, file_lines, error_num= itm[i][0].split('_')[0], itm[i][0].split('_')[1], itm[i][1]
    print(file_name,file_lines,error_num)
