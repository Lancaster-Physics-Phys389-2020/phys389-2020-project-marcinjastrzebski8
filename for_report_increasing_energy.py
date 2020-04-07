import matplotlib.pyplot as plt
from abs_draw_bob_paths import Draw_bob
from Save_Pandas import SavePandas
import numpy as np
import pandas as pd

sys = SavePandas(1,1,1,1)
"""
z01 = [0.2,0.2,0,0]
sys.Sys.set_initial(z01)
ham1 = sys.Sys.En_hamiltonian()
print(ham1)
sys.simulation(50000,0.001,z01)
sys.save_as('ham%s'%(ham1))

sys.Sys.set_initial([0,0,0,0])
ham0 = sys.Sys.En_hamiltonian()
print(ham0)
z02 = [0.7,0.4,0,0]
sys.Sys.set_initial(z02)
ham2 = sys.Sys.En_hamiltonian()
print(ham2)
sys.simulation(50000,0.001,z02)
sys.save_as('ham%s'%(ham2))

sys.Sys.set_initial([0,0,0,0])
z03 = [np.pi,np.pi,0.4,0]
sys.Sys.set_initial(z03)
ham3 = sys.Sys.En_hamiltonian()
print(ham3)
sys.simulation(50000,0.001,z03)
sys.save_as('ham%s'%(ham3))

sys.Sys.set_initial([0,0,0,0])
ham0 = sys.Sys.En_hamiltonian()
z04 = [np.pi,0,0.5,0.5]
sys.Sys.set_initial(z04)
ham4 = sys.Sys.En_hamiltonian()
print(ham4)
sys.simulation(50000,0.001,z04)
sys.save_as('ham%s'%(ham4))

sys.Sys.set_initial([0,0,0,0])

z05 = [np.pi,np.pi,1,0.5]
sys.Sys.set_initial(z05)
ham5 = sys.Sys.En_hamiltonian()
print(ham5)
sys.simulation(50000,0.001,z05)
sys.save_as('ham%s'%(ham5))
"""

sys.Sys.set_initial([0,0,0,0])
ham0 = sys.Sys.En_hamiltonian()
z04 = [1.5,0,1.3,2.2]
sys.Sys.set_initial(z04)
ham4 = sys.Sys.En_hamiltonian()
print(ham4)
sys.simulation(50000,0.001,z04)
sys.save_as('ham%s'%(ham4))

#z04 = [0.2,0.2,1,0] has -28.901997335237247 quasiperiodic cute
#z04 = [0.2,0.3,1,0.5] has -28.904690270064254 quasiperiodic
#z04 = [1,0.3,1,1] has -19.83987088323041 like inbetween quasiperiodic and chaotic
#z04 = [0.5,2,1,2] has -11.205454153984732 chaotic
#z04 = [2,2,2,2] has 14.484405096414271 chaotic begins to look periodic
#z04 = [0.3,0.7,1.2,0.4] has -26.37492155209082 quasiperiodic
#z04 = [1.1,0.9,1.2,1.9] has -13.272139782321354 chaotic
#z04 = [0.5,1,0.7,0.7] has -22.706688907551566 quasiperiodic
#z04 = [0.5,1,1.3,0.7] has -22.51852324430105 quasiperiodic
#z04 = [0.5,1,1.3,1.5] has -21.829565298244948 quasiperiodic
#z04 = [1,1,1.3,1.5] has -15.064069176044192 now this looks quasiperiodic? less chaotic than the other one
#z04 = [1.5,1,1.3,1.5] has -5.6926580937915485 chaotic
#z04 = [1.5,0,1.3,1.5] has -9.932504425501433 chaotic
#z04 = [1.5,0,1.3,2.2] has -8.66652252271125 chaotic






