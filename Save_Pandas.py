import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
from System_SA import SASystem
from System_SHM import SHMSystem
import pandas as pd


class SavePandas():
    def __init__(self,m1,m2,l1,l2,which = 0):
        self.pend1 = Oscillator(m1,l1)
        self.pend2 = Oscillator(m2,l2)
        if which ==1:
            self.choice = 1
            self.Sys = SASystem(self.pend1,self.pend2)
        elif which ==2:
            self.choice = 2
            self.Sys = SHMSystem(self.pend1,self.pend2)
        else:
            self.choice = 0
            self.Sys = System(self.pend1,self.pend2)

        self.pend_info = {'m1':m1,'m2':m2,'l1':l1,'l2':l2}


    def simulation(self,steps,timestep,initial_cond):
        self.Sys.set_initial(initial_cond)

        
        self.data = []
        for step in range(steps):
            self.data_time = step*timestep
            self.data_angle1 = self.Sys.Z[0]
            self.data_angle2 = self.Sys.Z[1]
            self.data_mom1 = self.Sys.Z[2]
            self.data_mom2 = self.Sys.Z[3]
            self.data_ham = self.Sys.En_hamiltonian()
            if self.choice == 0:
                if step ==0:
                    self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham,self.pend_info])
                else:
                    self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham])
            if self.choice == 1:
                self.omega1 = self.Sys.omega1
                self.omega2 = self.Sys.omega2
                if step ==0:
                    self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham,self.omega1,self.omega2,self.pend_info])
                else:
                    self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham])
            if self.choice == 2:
                self.T = self.Sys.T
                if step ==0:
                    self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham,self.T,self.pend_info])
                else:
                    self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham])

            self.Sys.RK(timestep)

        if self.choice == 0:
            self.df = pd.DataFrame(self.data,columns=['TIME','ANGLE 1','MOMENTUM 1', 'ANGLE 2', 'MOMENTUM 2', 'HAMILTONIAN','PENDULUM INFO'])
        if self.choice == 1:
            self.df = pd.DataFrame(self.data,columns=['TIME','ANGLE 1','MOMENTUM 1', 'ANGLE 2', 'MOMENTUM 2', 'HAMILTONIAN','FREQ 1','FREQ 2','PENDULUM INFO'])
        if self.choice == 2:
            self.df = pd.DataFrame(self.data,columns=['TIME','ANGLE 1','MOMENTUM 1', 'ANGLE 2', 'MOMENTUM 2', 'HAMILTONIAN','PERIOD','PENDULUM INFO'])

        

    def save_as(self,name = 'name'):
            self.df.to_pickle('%s.csv'%name)
