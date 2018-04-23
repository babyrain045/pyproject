import numpy as np
import pandas as pd

def max_min_scale(filename):
    filename_ = filename+'.xls'
    a = pd.read_table(filename_)
    index = a['name']
    a = a.set_index('name')
    pre_data = np.array(a)
    amin, amax = pre_data.min(), pre_data.max()
    pre_data = (pre_data - amin) / (amax - amin)
    print(pre_data)
    c = pd.DataFrame(pre_data,index= index,columns=index)
    c.to_excel(filename+'_scaled.xls')
    return c

max_min_scale('coor_dm')
max_min_scale('Hmarker_Distance_Matrix')
max_min_scale('snvNaNreplacedm')

