import numpy as np
from System_SA import SASystem
from Oscillator_class import Oscillator
import math
import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw

class Draw_beats(AbstractDraw):
    def get_dataset(self,dataset = 'file'):
        super().get_dataset(dataset)
        self.omega1 = self.data['FREQ 1'][0]
        self.omega2 = self.data['FREQ 2'][0]
        self.pend1 = Oscillator(self.m1,self.l1)
        self.pend2 = Oscillator(self.m2,self.l2)
        self.sys_w_beats = SASystem(self.pend1,self.pend2)

    def draw(self):
        for point in range(len(self.time)):
            self.x.append(self.time[point])
            self.y.append(self.data['ANGLE 1'][point])
        angl2= []
        for i in range(len(self.time)):
            angl = self.sys_w_beats.angles(self.time[i],self.data['ANGLE 2'][0])
            angl2.append(angl[0])
        plt.plot(self.x,self.y)
        plt.plot(self.x,angl2,linestyle ='dashed')
        
        plt.plot()