import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_pickle('shm.csv')
len1 = data['PENDULUM INFO'][0]['l1']
len2 = data['PENDULUM INFO'][0]['l2']
m1 = data['PENDULUM INFO'][0]['m1']
m2 = data['PENDULUM INFO'][0]['m2']
x1vals=[]
y1vals=[]
x2vals=[]
y2vals=[]
timestep = data['TIME'][1]



for i in range(len(data['TIME'])):

    x1 = len1*np.sin(data['ANGLE 1'][i])
    x2 = x1 + len2*np.sin(data['ANGLE 2'][i])
    y1 = -len1*np.cos(data['ANGLE 1'][i])
    y2 = y1-len2*np.cos(data['ANGLE 2'][i])
    x1vals.append(x1)
    x2vals.append(x2)
    y1vals.append(y1)
    y2vals.append(y2)

    if i %10 ==0:
        plt.plot([0,x1],[0,y1],linewidth = 1)
        plt.plot([x1,x2],[y1,y2],linewidth = 1)
        plt.plot(x1,y1,'bo',markersize = m1)
        plt.plot(x2,y2,'ro',markersize = m2)
        plt.axis([-2,2,-2,0.5]) 

axes = plt.gca() #get current axes
axes.set_ylim([-(len1+len2),(len1+len2)])
axes.set_xlim([-(len1+len2),(len1+len2)])
plt.xlabel('x')
plt.ylabel('y')        
plt.show()








