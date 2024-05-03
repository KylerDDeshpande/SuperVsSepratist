# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:51:08 2024

@author: kyler
"""
# importing models
import pandas as pd

# importing the dataset
data=pd.read_csv('happy.csv')

# fixing columns names and droping
data=data.rename(columns={'Ladder score':'Happyness','Explained by: Log GDP per capita':'GDP','Explained by: Social support':'Social','Explained by: Healthy life expectancy':'Health','Explained by: Freedom to make life choices':'Choices','Explained by: Generosity':'Generosity','Explained by: Perceptions of corruption':'Corruption','Dystopia + residual':'Dystopia'})
drop=['Unnamed: 0','upperwhisker','lowerwhisker']
data=data.drop(columns=drop)

# List of countries with sepratist movements
LSM=['Canada','United Kingdom','Belgium','Spain','Cyprus','Pakistan','North Cyprus','Iraq','Ukraine','India',]
SSM=['Hong Kong S.A.R. of China','Lebonon','Congo (Kinshasa)','Brazil','Iran','Turkey','Greece','Palestinian Territories','Germany','Morocco','China']

# creating a trim dataset
sep_lar=data['Country name'].isin(LSM)
dwlsp=data[sep_lar==False]
sep_sm=dwlsp['Country name'].isin(SSM)
trim=dwlsp[sep_sm==False]

# Calculationg for growth for every region for every category
trim2=trim.set_index(['Country name'])
avgs=trim2.groupby(['year','Regional indicator']).mean()
avg20=avgs.xs(2020,level='year')
diff=avgs-avg20
growth=diff.div(avg20)

# dataset of only the sepratist movements
LSD_trim=data['Country name'].isin(LSM)
LSD=data[LSD_trim==True]
SSD_trim=data['Country name'].isin(SSM)
SSD=data[SSD_trim==True]

# Calculating for growth for large sepratist movement
LSD2=LSD.set_index(['Country name'])
avg_LS=LSD2.groupby(['year','Regional indicator']).mean()
avg20_LS=avg_LS.xs(2020,level='year')
dif_LS=avg_LS-avg20_LS
growth_LS=dif_LS.div(avg20_LS)

# Calculating for growth for small sepratist movement
SSD2=SSD.set_index(['Country name'])
avg_SS=SSD2.groupby(['year','Regional indicator']).mean()
avg20_SS=avg_SS.xs(2020,level='year')
dif_SS=avg_SS-avg20_SS
growth_SS=dif_SS.div(avg20_SS)

# exporting the data
growth.to_csv('regional_change.csv')
growth_LS.to_csv('large_sep_change.csv')
growth_SS.to_csv('small_sep_change.csv')