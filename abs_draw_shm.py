import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw

class Draw_shm(AbstractDraw):
    def get_dataset(self,dataset = 'file'):
        super().get_dataset(dataset)
        self.T = self.data['PERIOD']

    def draw(self):
        for point in range(len(self.time)):
            self.x.append(self.time[point])
            self.y.append(self.data['ANGLE 2'][point])
        plt.plot(self.x,self.y)
    