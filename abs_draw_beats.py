import numpy as np
from System_B import SystemB
from Oscillator_class import Oscillator
import math
import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw


"""
NOT NEEDED FOR REPORT
"""
"""
This class can draw theoretical paths for the analytical small angle cases
with beats. 
User can choose between the two angles.
"""

class Draw_beats(AbstractDraw):
    def get_dataset(self,dataset = 'file'):
        super().get_dataset(dataset)
        self.pend1 = Oscillator(self.m1,self.l1)
        self.pend2 = Oscillator(self.m2,self.l2)
        self.sys_w_beats = SystemB(self.pend1,self.pend2)

    def draw(self,choice = 0):
        if choice ==0:
            for point in range(len(self.time)):
                self.x.append(self.time[point])
                self.y.append(self.data['ANGLE 1'][point])
            plt.plot(self.x,self.y)
            self.x = []
            self.y = []
        else:
            for point in range(len(self.time)):
                self.x.append(self.time[point])
                self.y.append(self.data['ANGLE 2'][point])
            plt.plot(self.x,self.y)

        
    