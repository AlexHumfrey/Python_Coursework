{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#read vaccination progress csv file into python\n",
    "#load required packages\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import urllib.request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from urllib.request import urlopen"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "from zipfile import ZipFile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "downloading file\n"
     ]
    }
   ],
   "source": [
    "#download vacc prog data from github into working environment\n",
    "#to download directly from kaggle API would allow for more up to date data to be collected (but would require username and password authentication)\n",
    "import requests, zipfile, io\n",
    "print('downloading file')\n",
    "zip_file_url = 'https://github.com/AlexHumfrey/Python_Coursework/raw/main/archive%20(1).zip'\n",
    "r = requests.get(zip_file_url)\n",
    "z = zipfile.ZipFile(io.BytesIO(r.content))\n",
    "z.extractall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#read in csv data\n",
    "filepath = '/Users/alexhumfrey/Documents/Loughborough/Semester 2 Modules/Python_Coursework/country_vaccinations.csv'\n",
    "df = pd.read_csv(filepath)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>people_fully_vaccinated_per_hundred</th>\n",
       "      <th>daily_vaccinations_per_million</th>\n",
       "      <th>vaccines</th>\n",
       "      <th>source_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>NaN</td>\n",
       "      <td>57.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>NaN</td>\n",
       "      <td>63.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>NaN</td>\n",
       "      <td>68.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>NaN</td>\n",
       "      <td>74.0</td>\n",
       "      <td>Oxford/AstraZeneca</td>\n",
       "      <td>Government of Afghanistan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    people_fully_vaccinated_per_hundred  daily_vaccinations_per_million  \\\n",
       "10                                  NaN                            57.0   \n",
       "11                                  NaN                            63.0   \n",
       "12                                  NaN                            68.0   \n",
       "13                                  NaN                            74.0   \n",
       "14                                  NaN                            74.0   \n",
       "15                                  NaN                            74.0   \n",
       "16                                  NaN                            74.0   \n",
       "17                                  NaN                            74.0   \n",
       "18                                  NaN                            74.0   \n",
       "19                                  NaN                            74.0   \n",
       "\n",
       "              vaccines                source_name  \n",
       "10  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "11  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "12  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "13  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "14  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "15  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "16  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "17  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "18  Oxford/AstraZeneca  Government of Afghanistan  \n",
       "19  Oxford/AstraZeneca  Government of Afghanistan  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df.head()\n",
    "\n",
    "#df.tail()\n",
    "\n",
    "#random sample of 5 rows from dataframe\n",
    "#df.sample(n=5, random_state = 1)\n",
    "\n",
    "# select rows and columns to view\n",
    "df.iloc[10:20,10:14]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['country',\n",
       " 'iso_code',\n",
       " 'date',\n",
       " 'total_vaccinations',\n",
       " 'people_vaccinated',\n",
       " 'people_fully_vaccinated',\n",
       " 'daily_vaccinations_raw',\n",
       " 'daily_vaccinations',\n",
       " 'total_vaccinations_per_hundred',\n",
       " 'people_vaccinated_per_hundred',\n",
       " 'people_fully_vaccinated_per_hundred',\n",
       " 'daily_vaccinations_per_million',\n",
       " 'vaccines',\n",
       " 'source_name',\n",
       " 'source_website']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#list of variables\n",
    "list(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#rename df columns\n",
    "#df.rename(columns={'text','TEXT'}, inplace=TRUE)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#select columns to work with for our purposes\n",
    "#specify chunks of columns, last number in the range not included in the generated list of numbers\n",
    "\n",
    "#vacprog_data = df.iloc[:,np.r_[0:3, 15:19, 27, 100, 103:107]]\n",
    "\n",
    "#vavprog_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#df.info()\n",
    "#df.shape\n",
    "# summary statistics of a specific column\n",
    "#df[[\"...\"]].describe()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
