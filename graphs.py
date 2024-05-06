# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:08:26 2024

@author: kyler
"""

# importing models
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=300
from scipy.stats import ttest_ind
import seaborn as sns
sns.set_theme(style='white')

# importing data
base=pd.read_csv('regional_change.csv')
large=pd.read_csv('large_sep_change.csv')
small=pd.read_csv('small_sep_change.csv')

# ttest to determine which variables to look at
print(f"Happyness T-stat: {ttest_ind(base['Happyness'],large['Happyness'])}")
print(f"GDP T-stat: {ttest_ind(base['GDP'],large['GDP'])}")
print(f"Social T-Stat: {ttest_ind(base['Social'],large['Social'])}")
print(f"Health T-Stat: {ttest_ind(base['Health'],large['Health'])}")
print(f"Choices T-Stat: {ttest_ind(base['Choices'],large['Choices'])}")
print(f"Generosity T-Stat: {ttest_ind(base['Generosity'],large['Generosity'])}")
print(f"Corruption T-Stat: {ttest_ind(base['Corruption'],large['Corruption'])}")
print('Varibles with the highest t-values and lowest p-values: Generosity, Choices, and Corruption')

# test to determine which regions to look at
var=base.query('year==2024')
var.plot.barh(y='Happyness',x='Region')
print('Regions to look: South Asia, Commonwealth of Independent States, and North America and ANZ')

# graph number 1: base 'happyness' by region
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Happyness',hue='Region',data=base)
ax.set_title('Happyness Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('happyness_by_region.png')

# graph number 2: base vs large and small by generosity in general
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Generosity', label='base', data=base, errorbar=None)
sns.lineplot(x='year',y='Generosity', label='large', data=large, errorbar=None)
sns.lineplot(x='year',y='Generosity', label='small', data=small, errorbar=None)
ax.set_title('Generosity Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('generosity_by_type.png')

# graph number 3: base vs large and small by choices in general
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Choices', label='base', data=base, errorbar=None)
sns.lineplot(x='year',y='Choices', label='large', data=large, errorbar=None)
sns.lineplot(x='year',y='Choices', label='small', data=small, errorbar=None)
ax.set_title('Choices Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('choices_by_type.png')

# graph number 4: base vs large and small by corruption in general
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Corruption', label='base', data=base, errorbar=None)
sns.lineplot(x='year',y='Corruption', label='large', data=large, errorbar=None)
sns.lineplot(x='year',y='Corruption', label='small', data=small, errorbar=None)
ax.set_title('Corruption Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('corruption_by_type.png')

# Creating small dataset by Region only
SA_B=base.query("Region=='South Asia'")
SA_L=large.query("Region=='South Asia'")
SA_S=small.query("Region=='South Asia'")
CIS_B=base.query("Region=='Commonwealth of Independent States'")
CIS_L=large.query("Region=='Commonwealth of Independent States'")
CIS_S=small.query("Region=='Commonwealth of Independent States'")
NA_B=base.query("Region=='North America and ANZ'")
NA_L=large.query("Region=='North America and ANZ'")
NA_S=small.query("Region=='North America and ANZ'")

# graph number 5: basic vs large and small by generosity in South Asia
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Generosity', label='base', data=SA_B)
sns.lineplot(x='year',y='Generosity', label='large', data=SA_L)
sns.lineplot(x='year',y='Generosity', label='small', data=SA_S)
ax.set_title('Generosity in South Asia')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('generosity_in_South_Asia.png')

# graph number 6: base vs large and small by generosity in Commonwealth of Independent States
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Generosity', label='base', data=CIS_B)
sns.lineplot(x='year',y='Generosity', label='large',data=CIS_L)
sns.lineplot(x='year',y='Generosity', label='small', data=CIS_S)
ax.set_title('Generosity in Commonwealth of Independent States')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('generosity_in_Commonwealth_of_Independent_States.png')

# graph number 7: base vs large and small by generosity in North America and ANZ
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Generosity', label='base', data=NA_B)
sns.lineplot(x='year',y='Generosity', label='large',data=NA_L)
sns.lineplot(x='year',y='Generosity', label='small', data=NA_S)
ax.set_title('Generosity in North America and ANZ')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('generosity_in_North_America_and_ANZ.png')

# graph number 8: base vs large and small by choices in South Asia
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Choices', label='base', data=SA_B)
sns.lineplot(x='year',y='Choices', label='large', data=SA_L)
sns.lineplot(x='year',y='Choices', label='small', data=SA_S)
ax.set_title('Choices in South Asia')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('choices_in_South_Asia.png')

# graph number 9: base vs large and small by choices in Commonwealth of Independent States
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Choices', label='base', data=CIS_B)
sns.lineplot(x='year',y='Choices', label='large', data=CIS_L)
sns.lineplot(x='year',y='Choices', label='small', data=CIS_S)
ax.set_title('Choices in Commonwealth of Independent States')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('choices_in_Commonwealth_of_Independent_States.png')

# graph number 10: base vs large and small by choices in North America and ANZ
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Choices', label='base', data=NA_B)
sns.lineplot(x='year',y='Choices', label='large', data=NA_L)
sns.lineplot(x='year',y='Choices', label='small', data=NA_S)
ax.set_title('Choices in North America and ANZ')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('choices_in_North_America_and_ANZ.png')

# graph number 11: base vs large and small by corruption in South Asia
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Corruption', label='base', data=SA_B)
sns.lineplot(x='year',y='Corruption', label='large', data=SA_L)
sns.lineplot(x='year',y='Corruption', label='small', data=SA_S)
ax.set_title('Corruption in South Asia')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('corruption_in_South_Asia.png')

# graph number 12: base vs large and small by corruption in Commonwealth of Independent States
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Corruption', label='base', data=CIS_B)
sns.lineplot(x='year',y='Corruption', label='large', data=CIS_L)
sns.lineplot(x='year',y='Corruption', label='small', data=CIS_S)
ax.set_title('Corruption in Commonwealth of Independent_States')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('corruption_in_Commonwealth_of_Independent States.png')

# graph number 13: base vs large and small by corruption in North America and ANZ
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Corruption', label='base', data=NA_B)
sns.lineplot(x='year',y='Corruption', label='large', data=NA_L)
sns.lineplot(x='year',y='Corruption', label='small', data=NA_S)
ax.set_title('Corruption in North America and ANZ')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('corruption_in_North_America_and_ANZ.png')