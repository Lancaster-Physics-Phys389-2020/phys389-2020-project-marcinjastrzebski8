import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from collections import OrderedDict
seismic = cm.get_cmap('seismic',512)
colors_d = seismic(np.linspace(0,1,512))
the_color = cm.get_cmap('inferno',512)
colors = the_color(np.linspace(0,1,512))
flipdata1 = pd.read_pickle('ttf_full_0_0001.csv')
flipdata = pd.read_pickle('ttf_full_0_004_long.csv')
print(flipdata) #print for checking
print(flipdata1)

#ttf = [] use for separated
ang1 = flipdata['ANGLE 1']
ang2 = flipdata['ANGLE 2']
fig, ax1 = plt.subplots()

"""
If you wanted to separate which one flipped you could start with this idea
for datapoint in range(len(flipdata['WHICH ONE'])):
    if flipdata['WHICH ONE'][datapoint] == 'pend1':
        ttf.append(flipdata['TIME TO FLIP'][datapoint]*(-1)+10)
    else:
        ttf.append(flipdata['TIME TO FLIP'][datapoint]-10)
"""


ax1.set_xlabel(R'$\theta_{1}$')
ax1.set_ylabel(R'$\theta_{2}$')

#c = ttf for separated
c = flipdata['TIME TO FLIP']
plt.scatter(ang1,ang2,s = 1,c=c,cmap=the_color) 
#plt.scatter(ang1,ang2,c=c,cmap = seismic) use for separated
cbar = plt.colorbar()
cbar.set_label('Time to flip')
plt.show()

#psm = axl.pcolormesh([ang1,ang2],cmap=copper, rasterized = True, vmin=-5,vmax=5) this from a different guide 
#fig.colorbar(psm,ax=axl)
#plt.show()
