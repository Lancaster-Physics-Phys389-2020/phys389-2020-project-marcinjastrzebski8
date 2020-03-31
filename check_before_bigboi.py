import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import pandas as pd
import matplotlib.pyplot as plt

m1 = 0.6
m2 = 0.9
l1 = 0.3
l2 = 0.3
pend1 = Oscillator(m1,l1)
pend2 = Oscillator(m2,l2)

time = 600000
timestep = 0.0001

Z=[3,2,0,0]

Sys=System(pend1,pend2)
Sys.set_initial(Z)
time_x = []
ham = []
for step in range(time):
    ham.append(Sys.En_hamiltonian())
    time_x.append(timestep*step)
    Sys.RK(timestep)
    if abs(Sys.Z[0]) >= np.pi or abs(Sys.Z[1]) >= np.pi:
        print(timestep*step)
        break


plt.plot(time_x,ham)
plt.show()