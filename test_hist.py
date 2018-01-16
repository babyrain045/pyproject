import matplotlib.pyplot as plt
import numpy as np
l=[0.13552943542232229, -0.023028677089246729, -0.01286011863462596, -0.021060221882724047, -0.0027266183388073503, -0.018056972525366668]
mn,sd=np.mean(l),np.std(l)
r2=0.96
plt.hist(l,bins=50)
plt.xlim(-1,1)
plt.ylim(-0.25,2)
plt.text(-0.75, 1.5, r'$\mu=%.4f,\ \sigma=%.4f$'%(mn,sd))

plt.annotate(r'R=%.4f'%r2,xy=(r2,0),xytext=(r2,0.5),arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
x = 0.96
y = 0
plt.plot(x,y,'*')
#plt.axis([-1,1,0,3])#xmin xmax ymin ymax
#plt.grid(True)#wang ge
plt.savefig("hist_test.pdf",dpi=200)
plt.show()
