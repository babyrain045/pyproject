import pandas as pd
import scipy
from scipy import spatial
import numpy as np
from numpy.linalg import norm
from scipy.spatial.distance import pdist
from itertools import combinations

df=pd.read_table("snv.txt",na_values='-')
df=df.fillna(-2)
df.index=df['name']
del df['name']

def nan_pdist_pd(data):
    dm=pd.DataFrame(0,index=data.index,columns=data.index,dtype=float)
    twosample=list(combinations(list(data.index),2))
    for i in twosample:
        sampleA, sampleB = i[0], i[1]
        flag = data.ix[sampleA] + data.ix[sampleB]
        flag = flag>=0
        dm[sampleB][sampleA]=dm[sampleA][sampleB] = norm(data.ix[sampleA][flag] - data.ix[sampleB][flag])
    return dm

dm=nan_pdist_pd(df)
print(dm)
dm.to_csv("snvNaNreplacedm.xls",sep="\t",index=True)
