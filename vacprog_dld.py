read vaccination progress csv file into python
#load required packages
import pandas as pd
import numpy as np
import urllib.request

from urllib.request import urlopen
from zipfile import ZipFile

#download vacc prog data from github into working environment
#to download directly from kaggle API would allow for more up to date data to be collected (but would require username and password authentication)
import requests, zipfile, io
print('downloading file')
zip_file_url = 'https://github.com/AlexHumfrey/Python_Coursework/raw/main/archive%20(1).zip'
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

#read in csv data
filepath = '/Users/alexhumfrey/Documents/Loughborough/Semester 2 Modules/Python_Coursework/country_vaccinations.csv'
df = pd.read_csv(filepath)
type(df)

df.head()

#df.tail()

#random sample of 5 rows from dataframe
#df.sample(n=5, random_state = 1)

# select rows and columns to view
df.iloc[10:20,10:14]

#list of variables
list(df)

#rename df columns
#df.rename(columns={'text','TEXT'}, inplace=TRUE)


#select columns to work with for our purposes
#specify chunks of columns, last number in the range not included in the generated list of numbers

#vacprog_data = df.iloc[:,np.r_[0:3, 15:19, 27, 100, 103:107]]

#vavprog_data.head()

#df.info()
#df.shape
# summary statistics of a specific column
#df[["..."]].describe()