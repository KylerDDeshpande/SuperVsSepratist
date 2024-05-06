# Sepratist Movements
Comparing states with separatist movements to the rest of the region they are within.
![Separatist Movements Around The World](Separatist_Movements_Around_The_World.png)

## Overview
Ever since the creation of the state, there have been those who do not wish to be a part of it. Either because they simply did not want to be ruled at all, because they viewed the current leader in a negative light, because they viewed the ruling party as too different from them or for any number of different reasons. This project will focus on the third reason for groups of people within a state who want to separate from a state to form their own state due to various often cultural differences (including but not limited to race/ethnicity, shared history, and religion). While many states have these groups they often don't get much attention until they are approaching a critical mass. Most outsider observers tie these movements not to their communication methods or long personal history but to shifts within the perception and policies of the ruling state. However, there has been very little research on what are the most important factors that lead to these movements gaining influence and if they vary by region. This project is the first elementary attempt to start to fill that gap using data from the World Happyness Survey and a list of popular separatist movements in the 2020s.

## Imputs
The data comes from the [World Happyness Survey](https://worldhappiness.report/data/) and is from the main data sets that they use for their interactive dashboard from 2020 through 2024. 

## Scripts
Three Python scripts are used for this project and should be run in the order that they are listed below.

1. happy.py

The first script is used to clean the data from the World Happiness Survey. Specifically, the script is built to merge the data sets for each year into one general data set (long ways) while making sure to keep the regional indicator for each of the different countries and then drop those states that only appear for some of the data sets.

1. seperate.py

The second script is used to separate the data created in happy.py into three different files one for the countries that have large separatist movements, one for the countries that have small separatist movements, and one more that counties the rest of the countries without separate movements who the World Happyness Survey has data on. The data is grouped by the regional indicator and year for later data analysis.

1. graphs.py

The third and final script is used to run some basic data analysis and to create various figures to display some of the data. The first two stats that were run were to determine which category/variable to look at and which region to look at for change over time. Afterward, graphs are produced to help visualize the change over time between the region as a whole and the states within those regions that had separatist movements when it came to important factors.

## Outputs
There are two main types of outputs. The first has two components a basic t-test run on all of the categories to determine which ones had the greatest difference between the base counties and the ones with separatist movements one graph showing, and a graph that displays the general happiness change over time for all the regions.

The second output is a series of thirteen graphs. Graph number one shows the base data change in a percentage in the happiness score by region. Graphs two through four compare the change in generosity, choices, and corruption between the base states, states with large separatist movements, and states with small separatist movements. Graphs number five, eight, and eleven do this same comparison but for states within the region of South Asia. Graphs number six, nine, and twelve do this but for the Commonwealth of Independent States, and graphs number seven, ten, and thirteen for North America and ANZ(Australia and New Zealand).

![General Happy Change Over Time By Region]
(happyness_by_region.png)

## Findings