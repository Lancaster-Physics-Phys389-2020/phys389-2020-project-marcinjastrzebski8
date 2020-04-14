import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import pandas as pd
import matplotlib.pyplot as plt

m1 = 1
m2 = 1
l1 = 0.1
l2 = 0.1
pend1 = Oscillator(m1,l1)
pend2 = Oscillator(m2,l2)

time = 500000
timestep = 0.002

Z=[3,3,0,0]

Sys=System(pend1,pend2)
Sys.set_initial(Z)
time_x = []
ham = []
for step in range(time):
    ham.append(Sys.En_hamiltonian())
    time_x.append(timestep*step)
    Sys.RK(timestep)


plt.plot(time_x,ham)
plt.show()