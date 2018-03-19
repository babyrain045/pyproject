import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model,discriminant_analysis,cross_validation


p = [0,0.1,0.3,0.5,0.8,1]
i = 0
d = []
d1 = 100
r = 1.4
while i<6:
    d.append(d1*(r**i));
    i = i + 1;
d_arr = np.array(d)
d_arr = d_arr.T

p_arr = np.array([[0,0.1,0.3,0.5,0.8,1]])
p_arr = p_arr.T
regr = linear_model.LinearRegression()
regr.fit(p_arr,d_arr)
k = regr.coef_
distance = regr.intercept_
x = [0,1]
y=[]
y = x*k + distance
print(k,distance)




plt.plot(p,d,'x')

plt.plot(x,y)
x = 0.5
y = 0.5*k +distance
y = float(y)
plt.scatter(x,y,s=50,color = 'r')
plt.annotate(r'k*x+distance=%s' %y,xy=(x,y),xycoords ='data', xytext=(+30, -30),textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.show()