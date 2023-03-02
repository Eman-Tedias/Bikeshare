import pandas as pd
import numpy as np
import datetime as dt
import usaddress


chicago = pd.read_csv('chicago.csv')
chicago['City'] = 'Chicago'
chicago['Start_Address'] = chicago['Start Station'] + chicago['City']

print(chicago['Start_Address'].value_counts())

#city_df.to_csv('Bikeshare_cities1.csv')