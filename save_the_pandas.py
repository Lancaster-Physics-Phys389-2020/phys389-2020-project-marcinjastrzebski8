import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import pandas as pd


"""
I want this program to be performing the time evolution of all my systems and saving all the data as pandas
"""
m1 = 1
m2 = 0.1
l1 = 1
l2 = 1
steps = 50000
timestep = 0.002

pendulum1 = Oscillator(m1,l1)
pendulum2 = Oscillator(m2,l2)
STBA = System(pendulum1,pendulum2) #system to be analysed
initial = [0,0.1,0,0] 
STBA.set_initial(initial)
#SSTBA.set_initial(initial)
pend_info = {'m1':m1,'m2':m2,'l1':l1,'l2':l2}
data = []
for step in range(steps):
    data_time = step*timestep
    data_angle1 = STBA.Z[0]
    data_angle2 = STBA.Z[1]
    data_mom1 = STBA.Z[2]
    data_mom2 = STBA.Z[3]
    data_ham = STBA.En_hamiltonian()
    if step == 0:
        data.append([data_time,data_angle1,data_mom1,data_angle2,data_mom2,data_ham,pend_info])
    else:    
        data.append([data_time,data_angle1,data_mom1,data_angle2,data_mom2,data_ham])
    STBA.RK(timestep)



df = pd.DataFrame(data,columns=['TIME','ANGLE 1','MOMENTUM 1', 'ANGLE 2', 'MOMENTUM 2', 'HAMILTONIAN','PENDULUM INFO'])

df.to_pickle('beats_test.csv')


