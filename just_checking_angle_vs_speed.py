import pandas as pd
import matplotlib.pyplot as plt


dat = pd.read_pickle('ham-8.66652252271125.csv')
x=[]
y=[]
for i in range(len(dat['TIME'])):
    x.append(dat['ANGLE 1'][i])
    y.append(dat['MOMENTUM 1'][i])

    
plt.plot(x,y)
plt.xlabel(R'$\theta_1$')
plt.ylabel(R'$p_1$')
plt.show()
