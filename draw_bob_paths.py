import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

readout = pd.read_pickle("small_ang1.csv")
len1 = 1
len2 = 1
x=[]
y=[]

#this could be colourmapped :>>>>

for i in range(len(readout['TIME'])):
    x1 = len1*np.sin(readout['ANGLE 1'][i])
    x2 = x1 + len2*np.sin(readout['ANGLE 2'][i])
    y1 = -len1*np.cos(readout['ANGLE 1'][i])
    y2 = y1-len2*np.cos(readout['ANGLE 2'][i])
    x.append(x2)
    y.append(y2)

plt.plot(x,y,'o',markersize = 2)
plt.show()








