from Oscillator_class import Oscillator
from System_SA import SASystem
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd


data = pd.read_pickle('beats_test.csv')
print(data)

m1 = data['PENDULUM INFO'][0]['m1']
m2 = data['PENDULUM INFO'][0]['m2']
l1 = data['PENDULUM INFO'][0]['l1']
l2 = data['PENDULUM INFO'][0]['l2']

pend1 = Oscillator(m1,l1)
pend2 = Oscillator(m2,l2)


sys_w_beats = SASystem(pend1,pend2)


time = []
ang1 = []
ang2 = []

for i in range(len(data['TIME'])):
    time.append(data['TIME'][i])
    ang1.append(data['ANGLE 1'][i])
    #ang2.append(data['ANGLE 2'][i])
#print(time)

angl1 = []

for i in (range(len(time))):
    angl = sys_w_beats.angles(time[i],data['ANGLE 2'][0])
    angl1.append(angl[0])



plt.plot(time,ang1)
plt.plot(time,angl1,linestyle='dashed')
#plt.plot(time,ang2)
plt.show()