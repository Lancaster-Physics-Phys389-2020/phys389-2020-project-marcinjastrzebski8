import matplotlib.pyplot as plt
from abs_draw_angle import Draw_angle
from Save_Pandas import SavePandas
import numpy as np
import pandas as pd


myangle1 = Draw_angle()
myangle1.get_dataset('path_uno.csv')
myangle1.name_axes('Time (s)',R'$\theta_2$ (rad)')

myangle1.draw(1)
myangle1.x = []
myangle1.y =[]
myangle1.get_dataset('path_dos.csv')
myangle1.draw(1)
plt.legend([R'$\theta_{2,0} = 1.9$',R'$\theta_{2,0} = 1.905$'])
plt.show()