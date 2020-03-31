import pytest
from Oscillator_class import Oscillator
from System_SA import SASystem
osc1 = Oscillator(1,1)
osc2 = Oscillator(1,1)
sample_sys = SASystem(osc1,osc2)
def test_normal_frequencies():
    assert abs(sample_sys.omega1 - 5.84) <0.01


