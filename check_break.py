from System import System
import pytest
from Oscillator_class import Oscillator
from Save_Pandas import SavePandas
pend1 = Oscillator(10**(-6),1)
pend2 = Oscillator(1,10**(-6))
#sys = System(pend1,pend2)
#sys.set_initial([1,1,1,1])
#for i in range(1000):
#sys.RK(0.0001)

evolve = SavePandas(10,1,10**(-3),1)

evolve.simulation(1000,0.001,[1,1,1,1])
