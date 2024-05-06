# Sepratist Movements
Comparing states with separatist movements to the rest of the region they are within.
![Separatist Movements Around The World](Separatist_Movements_Around_The_World.png)

## Overview
Ever since the creation of the state their has been those who do not wish to be a part of it. Either because they simple did not want to be ruled at all, because they viewed the current leader in a negative light, because they view the ruling party as to different from them, or for any number of different reasons. This project will be focusing on the third reason of groups of people within a state who want to seperate from a state to form their own state due to various often times cultural differences (including but not limited to race/ethnicity, shared history, and religion). While many states have these groups they often don't get much attention until they are approaching a critical mass. Most outsider observers tie these movements not to thier own communication methods or long personal history but to shifts within perception and policies of the ruling state. However, there has been very little research on what are the most important factors that lead to these movements gaining influence and if they vary by region. This project is a first and elementary attept to start to fill that gap using data from the World Happyness Survey and list of popular sepratist movement in the 2020s.

## Imputs
The data comes from the [World Happyness Survey](https://worldhappiness.report/data/) and is from there main data sets that they use for there interactive dashboard from 2020 through 2024. 

## Scripts
There are three python scripts that are used for this project and should be run in the order that they are listed below.

1. happy.py
The first script is used to clean the data from the World Happyness Survey. Specifically, the script is built to merge the data sets for each year into one general data set (long ways) while making sure to keep the regional indicator for each of the differnt countries and then droping thoses states which only appear for some of the data sets.

1. seperate.py
The secound script is used to seperate the data created in happy.py into three different files one for the countries who have large seperatist movements, one for the countries who have small seperatist movements, and one more that counties the rest of the countires without sepratist movements who the World Happyness SUrvey has data on. The data is grouped by the regionial indicator and year for later data analysis.

1. graphs.py
The third and final script is used to run some basic data anaylsis and to create various figures for the pruposes of displaying some of the data. The first two stats that are run where to determine which catigory/varaible to look at and which region to look at for change over time. Afterwards graphs are produce to help vizulize the change overtime between the region as a whole and the states within thoses regions that had speratist movements when it came to important factors.

## Outputs

## Findings