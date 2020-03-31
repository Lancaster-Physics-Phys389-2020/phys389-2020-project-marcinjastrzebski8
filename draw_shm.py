import numpy as np
import math
from Oscillator_class import Oscillator
from System_SHM import SHMSystem
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_pickle('small_dif_1.csv')
data1 = pd.read_pickle('small_dif_2.csv')

plt.plot(data['TIME'],data['ANGLE 2'])
plt.plot(data1['TIME'],data1['ANGLE 2'])
plt.xlabel(R'Time')
plt.ylabel(R'$\theta_{2}$')
plt.show()