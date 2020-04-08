import os
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt 
"""This program looks for the runs which I have visually categorised as chaotic no flip in the database scans_data
and accesses the hamiltonians for those runs to create a histogram"""

class Hams_cat():
    def __init__(self,cat_name = 'name'):
        self.cat = cat_name
        self.hams = []
        self.relevant_datasets =[]
        self.data_folder = Path('scans_data')
        for files in os.listdir('./scans/%s'%(self.cat)):
            """This loop takes the names of the runs in the category chaotic no flip"""
            root, ext = os.path.splitext(files) #get rid of the png extension
            data = root +'.csv' #add csv to the name
            self.relevant_datasets.append(data) #store in relevant_datasets
        for files in os.listdir('./scans_data'):
            """Now we access the main database and only gather hamiltonians
             of the runs which we categorised as chaotic no flip"""
            if files in self.relevant_datasets:
                file_to_open = self.data_folder / files
                data = pd.read_pickle(file_to_open)
                self.hams.append(data['HAMILTONIAN'][0])
        self.df = pd.DataFrame(self.hams,columns = ['HAMILTONIAN'])
        self.df.to_pickle('hams_%s.csv'%(self.cat))
