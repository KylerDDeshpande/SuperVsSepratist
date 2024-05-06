# Sepratist Movements
Comparing states with separatist movements to the rest of the region they are within.
![Separatist Movements Around The World](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/Other/Separatist_Movements_Around_The_World.png)

## Overview
Ever since the creation of the state, there have been those who do not wish to be a part of it. Either because they simply did not want to be ruled at all, because they viewed the current leader in a negative light, because they viewed the ruling party as too different from them or for any number of different reasons. This project will focus on the third reason for groups of people within a state who want to separate from a state to form their own state due to various often cultural differences (including but not limited to race/ethnicity, shared history, and religion). While many states have these groups they often don't get much attention until they are approaching a critical mass. Most outsider observers tie these movements not to their communication methods or long personal history but to shifts within the perception and policies of the ruling state. However, there has been very little research on what are the most important factors that lead to these movements gaining influence and if they vary by region. This project is the first elementary attempt to start to fill that gap using data from the World Happyness Survey and a list of popular separatist movements in the 2020s.

## Inputs
The data comes from the [World Happyness Survey](https://worldhappiness.report/data/) and is from the main data sets that they use for their interactive dashboard from 2020 through 2024. 

## Scripts
Three Python scripts are used for this project and should be run in the order that they are listed below.

1. happy.py

The first script is used to clean the data from the World Happiness Survey. Specifically, the script is built to merge the data sets for each year into one general data set (long ways) while making sure to keep the regional indicator for each of the different countries and then drop those states that only appear for some of the data sets.

2. seperate.py

The second script is used to separate the data created in happy.py into three different files one for the countries that have large separatist movements, one for the countries that have small separatist movements, and one more that counties the rest of the countries without separate movements who the World Happyness Survey has data on. The data is grouped by the regional indicator and year for later data analysis.

3. graphs.py

The third and final script is used to run some basic data analysis and to create various figures to display some of the data. The first two stats that were run were to determine which category/variable to look at and which region to look at for change over time. Afterward, graphs are produced to help visualize the change over time between the region as a whole and the states within those regions that had separatist movements when it came to important factors.

## Outputs
There are two main types of outputs. The first has two components a basic t-test run on all of the categories to determine which ones had the greatest difference between the base counties and the ones with separatist movements one graph showing, and a graph that displays the general happiness change over time for all the regions.

The second output is a series of thirteen graphs. Graph number one shows the base data change in a percentage in the happiness score by region.

![Happyness Scores Change Over Time By Region](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/happyness_by_region.png)

Graphs two through four compare the change in generosity, choices, and corruption between the base states, states with large separatist movements, and states with small separatist movements.
The one for corruption is shown below ![Corruption Scores Change Over Time](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/corruption_by_type.png)
 
Graphs number five, eight, and eleven do this same comparison but for states within the region of South Asia.
 The one for corruption in South Asia is shown below
![Corruption in South Asia](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/corruption_in_South_Asia.png)
 
Graphs number six, nine, and twelve do this but for the Commonwealth of Independent States, and graphs number seven, ten, and thirteen for North America and ANZ(Australia and New Zealand).
The ones for generosity in the Commonwealth of Independent States and choices for North America and ANZ are shown below
![Generosity in the Commonwealth of Independent States](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/generosity_in_Commonwealth_of_Independent_States.png)

![Choices in North America and ANZ](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/choices_in_North_America_and_ANZ.png)

## Findings
The data reveals some interesting findings when it comes to factors that change over time. After running the t-test, we see that the factors that changed the most over time between the base region states and the states with separatist movements are (in order of greatest difference): generosity (individuals within a state being generous to other individuals within the same state), choices (or freedom to make independent choices), and corruption (individuals who feel that their state's government is corrupt). Then when comparing changes between regions, we see that the regions that changed the most were South Asia (negatively), the Commonwealth of Independent States (positively), and North America and ANZ (positively).
Upon, analysis of the graphs that were generated by only looking at those three categories and three regions some patterns emerge.
1. General analysis reveals that both states with large and small spiritist movements are improving when it comes to generosity and choices in comparison with the base states. However, over the period that we have data there is a switch when it comes to corruption as states with large movements start with the lowest corruption and end up being the highest, and states with small separatist movements start with the highest and end up being the lowest.
1. South Asia the region that has had the worst change over time, states with large separatist movements are only doing worse than the base states when it comes to corruption.
1. The only other place where states with large separatist movements are doing worse over time in comparison to the base states is when it comes to choices in North America and ANZ.
1. There are large gaps between the base states and states with large separatist movements for corruption in both the Commonwealth of Independent States and South Asia.
1. There are smaller gaps between the base states and states with large separatist movements for choices for all regions and generosity in the Commonwealth of Independent States.
Thus, we see that when it comes to the three most important factors that change the happiness score for the regions over the period where we have the data, states with separatist movements are on average doing better than the base states when it comes to generosity and choices but is doing significantly worse when it comes to corruption. This would seem to imply that the people in states with separatist movements tend not to have much difficulties with their fellow countrymen but have great difficulties when it comes to the relationship between them and their government.

![Happyness by State Type](https://github.com/KylerDDeshpande/SuperVsSepratist/blob/main/happyness_by_type.png)
