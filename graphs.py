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
var.plot.barh(y='Happyness',x='Regional indicator')
print('Regions to look: South Asia, Commonwealth of Independent States, and North America and ANZ')

# graph number 1: basic 'happyness' by region
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Happyness',hue='Regional indicator',data=base)
ax.set_title('Happyness Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('happyness_by_region.png')

# graph number 2: basic vs large and small by generosity in general
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Generosity', data=base)
sns.lineplot(x='year',y='Generosity', data=large)
sns.lineplot(x='year',y='Generosity', data=small)
ax.set_title('Generosity Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('generosity_by_type.png')

# graph number 3: basic vs large and small by choices in general
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Choices', data=base)
sns.lineplot(x='year',y='Choices', data=large)
sns.lineplot(x='year',y='Choices', data=small)
ax.set_title('Choices Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('choices_by_type.png')

# graph number 4: basic vs large and small by corruption in general
fig,ax=plt.subplots()
sns.lineplot(x='year',y='Corruption', data=base)
sns.lineplot(x='year',y='Corruption', data=large)
sns.lineplot(x='year',y='Corruption', data=small)
ax.set_title('Corruption Scores Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Percent Change')
fig.tight_layout()
fig.savefig('corruption_by_type.png')

# graph number 5: basic vs large and small by generosity in #South Asia

# graph number 6: basic vs large and small by generosity in #Commonwealth of Independent States

# graph number 7: basic vs large and small by generosity in #North America and ANZ

# graph number 8: basic vs large and small by choices in #South Asia

# graph number 9: basic vs large and small by choices in #Commonwealth of Independent States

# graph number 10: basic vs large and small by choices in #North America and ANZ

# graph number 11: basic vs large and small by corruption in #South Asia

# graph number 12: basic vs large and small by corruption in #Commonwealth of Independent States

# graph number 13: basic vs large and small by corruption in #North America and ANZ