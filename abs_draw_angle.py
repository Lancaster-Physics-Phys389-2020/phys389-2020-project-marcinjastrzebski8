import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw

class Draw_angle(AbstractDraw):
    def draw(self,choice = 0):
        for point in range(len(self.time)):
            self.x.append(self.time[point])
            if choice ==0:
                self.y.append(self.data['ANGLE 1'][point])
            else:
                self.y.append(self.data['ANGLE 2'][point])
        plt.plot(self.x,self.y,linewidth = 3)
    