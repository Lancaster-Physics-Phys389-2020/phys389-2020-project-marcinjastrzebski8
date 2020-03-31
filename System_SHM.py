from Oscillator_class import Oscillator
import numpy as np
import math
from System import System

"""
This is a special case of the double pendulum where the small angle approximation makes for an analytical solution
"""

class SHMSystem(System):

    #make it throw an exception when the set initial is not [SMALL,SMALL,0,0] (define small?)
    #and an exception if m1 is not small

    def __init__(self,Pendulum1,Pendulum2):
        if Pendulum1.mass > 10**(-3):
            raise Exception('The mass of the first pendulum must be negligible (no greater than 10^3). You passed m1 = %s'%(Pendulum1.mass))
        super().__init__(Pendulum1,Pendulum2)
        self.T = 2*np.pi*((self.first.length+self.second.length)/self.g)**(0.5)

    def set_initial(self,Z0 = np.array([0,0,0,0],dtype = float)):
        if Z0[0] >= 0.3 or Z0[1] >= 0.3 or Z0[2] !=0 or Z0[3] !=0:
            raise Exception('This system works only for initial conditions of the form [SMALL,SMALL,0,0] where SMALL means <0.3. You passed %s.' %(Z0))
        super().set_initial(Z0)
     
    
