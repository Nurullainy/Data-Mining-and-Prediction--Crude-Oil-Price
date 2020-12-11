# Data-Mining-and-Prediction--Crude-Oil-Price

The objective of this project is first to find hidden pattern of historical crude oil prices and real time crude oil price (for a certain time frame) on daily basis. I did web scrape news articles from online news websites and study how geopolitics, supply and demand can affects crude oil prices. These data will be analysed mainly using Python to predict crude oil prices and finally deploy it in web and mobile-app.

======================================================================================

This project consists of 5 parts with 5 milestones:

#### Milestone 1:
Acquisition of crude oil price data via web scrape using Scrapy and Selenium libraries

News article web scrape from online news website using Selenium and BeautifulSoup libraries

Selenium is required because some HTML elements involved JavaScript and can only be executed in the internet browser, and that JavaScript will grab data for a webpage.

Make sure chrome driver is downloaded, required by Selenium. Can be downloaded from https://sites.google.com/a/chromium.org/chromedriver/ 
Download chrome driver for version 80 (and above depend on your chrome's version). Put the chromedriver.exe in the directory of the project folder.

#### Milestone 2:
Management of data: store data into hive data warehouse or store data into data lake

#### Milestone 3:
Processing of data: accessing hive data warehouse or data lake using Python

#### Milestone 4:
Interpretation of data & Communication of Insights of data

Descriptive Analysis using Python D Tale library

#### Milestone 5:
Deployment in web (Flask) - Doing individual for this project

Predictive Analytics - Recurrent Neural Network

Deploy web application using Flask
