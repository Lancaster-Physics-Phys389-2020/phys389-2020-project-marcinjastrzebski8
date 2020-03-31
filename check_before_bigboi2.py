import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import pandas as pd


data = pd.read_pickle('time_to_flip.csv')
print(data)