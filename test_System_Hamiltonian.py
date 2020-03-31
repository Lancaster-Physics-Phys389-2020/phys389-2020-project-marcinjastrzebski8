import pytest
from Oscillator_class import Oscillator
from System import System
import numpy as np
import math

pend1 = Oscillator(1,1)
pend2 = Oscillator(1,1)
sample_system = System(pend1,pend2)
initial = [0,0,0,1]
sample_system.set_initial(initial)

def test_Hamiltonian():
    assert sample_system.En_hamiltonian() == -29.0




