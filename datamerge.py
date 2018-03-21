import pandas as pd
import csv
import numpy

import datetime
import glob, os
import re

# takes all the different data files to merge into one
path = "/Users/jaclyn/Desktop/CodeLouisville/Python_Data/olympics_project/input_data/"
os.chdir(path)
results = pd.DataFrame([])

# neutralizes all data, converts everything to lowercase and appends year
for counter, current_file in enumerate(glob.glob("*.csv")):
    namedf = pd.read_csv(current_file, encoding='iso-8859-1', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    namedf['Country'] = namedf.Country.astype(str)
    x = namedf[['City', 'Sport', 'Discipline', 'Athlete', 'Country', 'Gender', 'Event', 'Medal']].applymap(str.lower)
    x['Year'] = namedf.Year

    print(x)

    results = pd.concat([results, x])

# puts new dataset into an actual file
results.to_csv('/Users/jaclyn/Desktop/CodeLouisville/Python_Data/olympics_project/output_data/totalresults.csv',
               index=None,
               )

