

import pandas as pd

path = 'D:/Rui/kaggle/titanic'
train_data = pd.read_csv(path + '/test.csv')
pre_data = pd.DataFrame(train_data)
print(pre_data)