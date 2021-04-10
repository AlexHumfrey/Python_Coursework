#!/usr/bin/env python
# coding: utf-8

#read spss file into python

#load required packages
import pandas as pd
import pyreadstat
import numpy as np
import urllib.request


# download file from C19PRC Vaccine Hesitancy Data UK website
print('downloading file')
url = 'https://osf.io/g2hwn/download'
filepath = '/Users/alexhumfrey/Documents/Loughborough/Semester 2 Modules/Python_Coursework/survey_data.sav'
urllib.request.urlretrieve(url, path)

#two variables created dataframe and metadata object
# data from https://osf.io/g2hwn/
df, meta = pyreadstat.read_sav(filepath)

type(df)

df.head()

df.tail()

# random sample of 5 rows from dataframe
df.sample(n=5, random_state = 1)

# select rows and columns to view
df.iloc[10:20,100:106]

#list of variables
list(df)

type(meta)

#metadata object variable descriptions
print(meta.column_names_to_labels)

#metadata object variable value labels
print(meta.variable_value_labels)

#rename df columns
#df.rename(columns={'text','TEXT'}, inplace=TRUE)

#select columns to work with for our purposes

#specify chunks of columns, last number in the range not included in the generated list of numbers

survey_data = df.iloc[:,np.r_[0:3, 15:19, 27, 100, 103:107]]

survey_data.head()

df.info()

df.shape

# summary statistics of a specific column
df[["AgeCat"]].describe()


