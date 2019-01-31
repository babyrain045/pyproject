import pandas as pd
from sklearn import linear_model

train_X = pd.read_csv("delete1210.csv")
train_Y = pd.read_table("phenotype50.txt")
df_x = pd.DataFrame(train_X)
df_y = pd.DataFrame(train_Y)
df_x.set_index(["pos"],inplace=True)
df_y.set_index(["name"],inplace=True)
df_y = df_y[["glu0h","glu2h"]]
df = pd.merge(df_x,df_y,left_index=True,right_index=True)
df_y = df[['glu0h','glu2h']]

X_train = df_x
X_test = df_x[45:49]
Y_train = df_y
Y_test = df_y[45:49]

regr = linear_model.LinearRegression()
regr.fit(X_train,Y_train)


coeff_1 = regr.coef_[0]
coeff_2 = regr.coef_[1]

coeff_1 = map(abs,coeff_1)
coeff_2 = map(abs,coeff_2)
coeff_list_1 = []
coeff_list_2 = []
for i in coeff_1:
    coeff_list_1.append(i)
for i in coeff_2:
    coeff_list_2.append(i)

print(coeff_list_1.index(max(coeff_list_1)),coeff_list_2.index(max(coeff_list_2)))
print(coeff_list_1[coeff_list_1.index(max(coeff_list_1))],coeff_list_2[coeff_list_2.index(max(coeff_list_2))])

target = df_x.iloc[:,[coeff_list_1.index(max(coeff_list_1))]]


outfile = pd.DataFrame(regr.coef_)
outfile.to_csv('coefficient.txt',sep=' ')
target.to_csv('target_column.txt',sep=' ')
