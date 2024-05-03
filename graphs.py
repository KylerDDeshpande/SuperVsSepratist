# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:08:26 2024

@author: kyler
"""

# importing models
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=300
sns.set_theme(style='white')
from scipy.stats import ttest_ind

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

# ttest to determine which regions to look at
#print(f"Generosity T-Stat: {ttest_ind(base['Happyness'].where('Regional indicator'=='Central and Eastern Europe'),large['Happyness'].where('Regional indicator'=='Central and Eastern Europe'))}")


# graph number 1: basic 'happyness' by region
sns.lineplot(x='year',y='Happyness',hue='Regional indicator',data=base)

# graph number 2: basic vs large and small by generosity in general
fig,ax=plt.subplots()
base['Generosity'].plot(ax=ax)
large['Generosity'].plot(ax=ax)
small['Generosity'].plot(ax=ax)
fig.tight_layout()

# graph number 3: basic vs large and small by choices in general

# graph number 4: basic vs large and small by corruption in general

# graph number 5: basic vs large and small by generosity in #1

# graph number 6: basic vs large and small by generosity in #2

# graph number 7: basic vs large and small by generosity in #3

# graph number 8: basic vs large and small by choices in #1

# graph number 9: basic vs large and small by choices in #2

# graph number 10: basic vs large and small by choices in #3

# graph number 11: basic vs large and small by corruption in #1

# graph number 12: basic vs large and small by corruption in #2

# graph number 13: basic vs large and small by corruption in #3