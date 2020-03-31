from Save_Pandas import SavePandas
import pandas as pd
eh = SavePandas(0.1,10,1,1,1)
eh.simulation(10000,0.001,[0,0.2,0,0])
eh.save_as('check_raise_beat')

read = pd.read_pickle('check_raise_beat.csv')
print(read)
