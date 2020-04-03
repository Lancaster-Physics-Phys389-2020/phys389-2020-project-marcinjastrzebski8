import matplotlib.pyplot as plt
from abs_draw_beats import Draw_beats
from Save_Pandas import SavePandas
from System_B import SystemB
from Oscillator_class import Oscillator
import numpy as np
import pandas as pd


sys = SavePandas(1,1,1,1)
sys.simulation(10000,0.001,[0,0.1,0,0])
sys.save_as('beats_test')
dat = pd.read_pickle('beats_test.csv')

pend1 = Oscillator(1,1)
pend2 = Oscillator(1,1)
sysb = SystemB(pend1,pend2)
sysb.set_initial([0,0.1,0,0])
x=[]
y=[]

for i in np.linspace(0,10,10000):
    x.append(i)
    angl = sysb.angles(i,0.1)
    y.append(angl[0])

mybeat = Draw_beats()
mybeat.get_dataset('beats_test.csv')
mybeat.name_axes('Time (s)',R'$\theta_{1}$ (rad)')

mybeat.draw()
plt.plot(x,y,linestyle = 'dashed')
plt.legend(['Simulation','Theory'],loc=1)
mybeat.show()

sys1 = SavePandas(1,0.2,1,1)
sys1.simulation(30000,0.0005,[0,0.1,0,0])
sys1.save_as('beats_02')


mybeat1 = Draw_beats()
mybeat1.get_dataset('beats_02.csv')
mybeat1.name_axes('Time (s)',R'$\theta$ (rad)')

mybeat1.draw()
mybeat1.draw(1)
plt.legend([R'$\theta_{1}$',R'$\theta_{2}$'])

plt.show()

sys1 = SavePandas(1,2,1,1)
sys1.simulation(30000,0.0005,[0,0.1,0,0])
sys1.save_as('beats_2')


mybeat1 = Draw_beats()
mybeat1.get_dataset('beats_2.csv')
mybeat1.name_axes('Time (s)',R'$\theta$ (rad)')

mybeat1.draw()
mybeat1.draw(1)
plt.legend([R'$\theta_{1}$',R'$\theta_{2}$'])

plt.show()

sys1 = SavePandas(1,5,1,1)
sys1.simulation(30000,0.0005,[0,0.1,0,0])
sys1.save_as('beats_5')


mybeat1 = Draw_beats()
mybeat1.get_dataset('beats_5.csv')
mybeat1.name_axes('Time (s)',R'$\theta$ (rad)')

mybeat1.draw()
mybeat1.draw(1)
plt.legend([R'$\theta_{1}$',R'$\theta_{2}$'])

plt.show()

sys1 = SavePandas(1,10,1,1)
sys1.simulation(30000,0.0005,[0,0.1,0,0])
sys1.save_as('beats_10')


mybeat1 = Draw_beats()
mybeat1.get_dataset('beats_10.csv')
mybeat1.name_axes('Time (s)',R'$\theta$ (rad)')

mybeat1.draw()
mybeat1.draw(1)
plt.legend([R'$\theta_{1}$',R'$\theta_{2}$'])

plt.show()


