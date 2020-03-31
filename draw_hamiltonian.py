#ABORT THE MISSION - NOT NEEDED

from Oscillator_class import Oscillator
from System import System
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


m1 = 1
m2 = 1
l2 = 1
l1 = 1

pend1 = Oscillator(m1,l1)
pend2 = Oscillator(m2,l2)
#Z1 = [0,0,0,45**(0.5)]
#Z2 = [(np.pi)/3,0,0,(7/2)*(5**(0.5))]
#Z1 = [(np.pi)/2,-(np.pi)/3,0,0]
Z1 = [np.pi,2,0,0]
#Z2 = [(np.pi)/3,-(np.pi)/3,0,0]
sys1 = System(pend1,pend2)
#sys2 = System(pend1,pend2)
sys1.set_initial(Z1)
#sys2.set_initial(Z2)

x_is_angle = []
y_is_p = []
x2_is_angle = []
y2_is_p = []
Ham1 = []
time = 15000
timestep = 0.002
#Ham2 = []
t = []
for i in range(time):
    t.append(i*timestep)
    Ham1.append(sys1.En_hamiltonian())
    x_is_angle.append(sys1.Z[0])
    y_is_p.append(sys1.Z[2])
    sys1.RK(timestep)
    #Ham2.append(sys2.En_hamiltonian())
    #x2_is_angle.append(sys2.Z[0])
    #y2_is_p.append(sys2.Z[2])
    #sys2.RK(0.0001)



plt.plot(t,Ham1)
#plt.plot(t,Ham2)
plt.ylabel('Hamiltonian')
plt.xlabel('time')
plt.show()


