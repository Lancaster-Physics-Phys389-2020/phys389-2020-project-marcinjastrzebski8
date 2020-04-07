import matplotlib.pyplot as plt
import pandas as pd


dat = pd.read_pickle('ham83.49145650463575.csv')
t = []
ham = []
for i in range(len(dat['TIME'])):
    t.append(dat['TIME'][i])
    ham.append(dat['HAMILTONIAN'][i])

plt.plot(t,ham)
plt.ylim(ham[0]-1,ham[0]+1)
plt.show()



