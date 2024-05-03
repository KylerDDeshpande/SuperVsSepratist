# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:58:40 2024

@author: kyler
"""

# importing models
import pandas as pd

# inputting all the data
# putting all the csv files into one dataframe
data={}
data[2020]=pd.read_csv('World_Happy_2020.csv')
data[2021]=pd.read_csv('World_Happy_2021.csv')
data[2022]=pd.read_csv('World_Happy_2022.csv')
data[2023]=pd.read_csv('World_Happy_2023.csv')
data[2024]=pd.read_csv('World_happy_2024.csv')

# fixing columns names
data[2022]=data[2022].rename(columns={'Country':'Country name','Happiness score':'Ladder score','Whisker-high':'upperwhisker','Whisker-low':'lowerwhisker','Dystopia (1.83) + residual':'Dystopia + residual','Explained by: GDP per capita':'Explained by: Log GDP per capita'})
data[2024]=data[2024].rename(columns={'Happiness score':'Ladder score'})

# combining them all together
stacked=pd.concat(data)
stacked=stacked.reset_index(0)
stacked=stacked.rename(columns={'level_0':'year'})

# dropping one extra column
stacked=stacked.drop(columns='RANK')

# creating a new dataframe that only has the columns that are in every year
drop_col=['Standard error of ladder score','Logged GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption','Ladder score in Dystopia']
clean=stacked.drop(columns=drop_col)

## fixing the regional indicator column

# seperating the dataframe to batter manage the changes
regdef=clean.query('year==2020')[['Country name','Regional indicator']]
fixed=clean.drop(columns='Regional indicator')

# Changing the names of some states
cn=fixed['Country name']
cn=cn.str.replace('*','')
cn=cn.replace('Turkiye','Turkey')
cn=cn.replace('Eswatini, Kingdom of','Swaziland')
cn=cn.replace('Eswatini','Swaziland')
cn=cn.replace('State of Palestine','Palestinian Territories')
cn=cn.replace('Congo','Congo (Kinshasa)')
fixed['Country name']=cn

# Dropping two entries
bad_state=fixed['Country name'].isin(['Congo (Brazzaville)','xx'])
fixed=fixed[bad_state==False]

# merging the indicators back on the dataframe
fixed=fixed.merge(regdef,validate='m:1',how='left',indicator=True)
print(fixed["_merge"].value_counts())

# adding a regional indicator to some states
cn=fixed['Country name']
ri=fixed['Regional indicator']
ri=ri.where(cn!='North Macedonia','Central and Eastern Europe')
ri=ri.where(cn!='Czechia','Commonwealth of Independent States')
fixed['Regional indicator']=ri

# sending out cleaned total dataset to a csv file
fixed=fixed.drop(columns='_merge')
fixed.to_csv('happy.csv')