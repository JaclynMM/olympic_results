import pandas as pd
import csv
import numpy

import datetime
import glob, os
import re

path = "/Users/jaclyn/Desktop/CodeLouisville/Python_Data/olympics_project/input_data/"
os.chdir(path)
results = pd.DataFrame([])

for counter, current_file in enumerate(glob.glob("*.csv")):
    namedf = pd.read_csv(current_file, encoding='iso-8859-1', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(namedf[['City', 'Sport', 'Discipline', 'Athlete', 'Country', 'Gender', 'Event', 'Medal']].applymap(str.lower))
    results = pd.concat([results, namedf])

results.to_csv('/Users/jaclyn/Desktop/CodeLouisville/Python_Data/olympics_project/output_data/totalresults.csv',
               index=None,
               )

