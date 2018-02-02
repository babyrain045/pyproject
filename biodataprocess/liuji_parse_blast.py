
from bottle import *
from pandas import pandas as pd
import webbrowser


def calculate(df_file,type_selected,thred):
    non_self_dict = {}
    count = 0
    if type_selected == 'EValue':
        type_num = 10
    elif type_selected == 'Identity':
        type_num = 2
    else:
        type_num = 11

    for i in df_file.index:

        name_1 = df_file.loc[count, 0]
        name_2 = df_file.loc[count, 1]
        e_value = df_file.loc[count, type_num]
        count += 1
        if name_1 == name_2:
            continue

        else:
            if float(e_value) >= float(thred):
                non_self_dict.setdefault(name_1, []).append(e_value)
            else:
                continue
   # print(non_self_dict)
    outfile = open('./upload/liuji_blast_%s_%s' % (type_selected,thred), 'w')
    outfile.write('Query_protein\tQualified\n')
    for i in non_self_dict:
        num = len(non_self_dict.get(i))
        outfile.write('%s\t%s\n' % (i, num))
    outfile.close()

base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径
upload_path = os.path.join(base_path, 'upload')  # 上传文件目录

if not os.path.exists(upload_path):
    os.makedirs(upload_path)




@route('/', method='GET')
@route('/upload', method='GET')
@route('/index.html', method='GET')
@route('/upload.html', method='GET')
def index():
    return static_file('upload.html',root='.')

@route('/upload', method = 'POST')
def do_upload():
    filedata = request.files.get('fileField')
    type_selected = request.forms.get('type')
    threshold = request.forms.get('Threshold')

    if filedata.file:
        file_name = os.path.join(upload_path, filedata.filename)
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
            filedata.save(file_name)  # 上传文件写入
            orig_file = filedata.file
            df_file = pd.read_table(orig_file, header=None)
            calculate(df_file,type_selected,threshold)

        except IOError:
            return '上传文件失败'
        return '上传文件成功, 文件名: {}'.format(file_name)
    else:
        return '上传文件失败'



@route('/favicon.ico', method='GET')
def server_static():
    """处理网站图标文件, 找个图标文件放在脚本目录里"""
    return static_file('favicon.ico', root=base_path)


@error(404)
def error404(error):
    """处理错误信息"""
    return '404 发生页面错误, 未找到内容'

webbrowser.open("http://127.0.0.1:8080/")
run(port=8080, reloader=False)  # reloader设置为True可以在更新代码时自动重载





