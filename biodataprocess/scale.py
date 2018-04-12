import numpy as np
import pandas as pd
from ete3 import Tree


from sklearn import preprocessing
def max_min_scale(filename):
    filename_ = filename+'.xls'
    a = pd.read_table(filename_)
    index = a['name']
    a = a.set_index('name')
    scaler = preprocessing.MinMaxScaler()
    a_scaler = scaler.fit_transform(a)
    c = pd.DataFrame(a_scaler,index= index,columns=index)
    c.to_excel(filename+'_scaled.xls')
    return c
matrix = max_min_scale('coor_dm')


