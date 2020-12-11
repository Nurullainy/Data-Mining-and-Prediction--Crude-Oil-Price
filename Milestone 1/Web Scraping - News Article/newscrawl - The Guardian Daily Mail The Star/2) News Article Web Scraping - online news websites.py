#!/usr/bin/env python
# coding: utf-8

# ## WQD 7005 Data Mining 
# ## Project Title: Crude Oil Price Prediction
# ### Milestone 1: Data Extraction - News article from online websites
# 
# 
# ##### Team member: 
# 1) Nurullainy binti Mat Rashid 17036591
# 
# 2) Nor Asmidah Binti Mohd Arshad 17021881
# 
# 

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import datetime
import uuid


# ### Working out which pages to scrape
# 
# Obtain list of news from the one of the popular news article website, The Guardian websites. Website: https://www.theguardian.com/uk
# 


# url definition

url = "https://www.theguardian.com/uk"
response = requests.get(url)
response.status_code
print(response)

# Save the cover page content as guardianpage
guardianpage = response.content


# ### Using BeautifulSoup to parse the HTML content
# 
# There are several packages in Python that allow us to scrape information from webpages. We’ll use a Python module called BeautifulSoup, the most common web scraping module for Python.


# Parsing HTML content
page_soup = BeautifulSoup(guardianpage, 'html.parser')

# News identification
guardian_news = page_soup.find_all('h3', class_='fc-item__title')


# number of news article
print('Number of news article: {}' .format(len(guardian_news)))


# Now we have a list in which every element is a news article:

# Lets try to see 5th news article

print(guardian_news[4].prettify())


# ### Extract the text from the articles - web scraping technique

# First, we'll define the number of articles we want:

number_of_articles = len(guardian_news)


# Create lists for news content: news article links, titles, news id, dates & time
list_links_g = []
list_titles_g = []
list_newsid_g = []
list_dates_g = []
list_websites_g = []

for n in np.arange(0, number_of_articles):
        
    # We need to ignore "live" pages since they are not articles
    if "live" in guardian_news[n].find('a')['href']:  
        continue
    
    # Getting the link of the article
    link_g = guardian_news[n].find('a')['href']
    list_links_g.append(link_g)
    
    # Getting the title
    title_g = guardian_news[n].find('a').get_text()
    list_titles_g.append(title_g)
    
    # Creating unique ID
    NewsId_g = uuid.uuid1()
    list_newsid_g.append(NewsId_g)
    
    # Getting the date and time
    now = datetime.now()
    dateNews = now.strftime("%d/%m/%Y, %H:%M:%S")
    if len(list_dates_g) <= len(list_titles_g):
        list_dates_g.append(str(dateNews))
    else:
        stop()
        
    # Getting website's name
    websites_g = 'The Guardian'
    if len(list_websites_g) <= len(list_titles_g):
        list_websites_g.append(websites_g)
    else:
        stop()


# ### Save extracted data into Pandas dataframe
# 
# Save extracted data into a dataset with the title and the link

# df_show_info
df_show_guardian = pd.DataFrame(
    {'Article Title': list_titles_g,
     'Article Link': list_links_g,
     'News ID': list_newsid_g,
     'Date': list_dates_g,
     'Website': list_websites_g
    })


df_show_guardian


# url definition for DailyMail

url = "https://www.dailymail.co.uk"
r2 = requests.get(url)
r2.status_code

# Save the cover page content as dailymailpage
dailymailpage = r2.content


# Parsing HTML content
page_soup = BeautifulSoup(dailymailpage, 'html.parser')

# News identification
dailymail_news = page_soup.find_all('h2', class_='linkro-darkred')
print('Number of news article: {}' .format(len(guardian_news)))


number_of_articles = len(dailymail_news)


# Create lists for news content, links and titles
list_links_d = []
list_titles_d = []
list_newsid_d = []
list_dates_d = []
list_websites_d = []

for n in np.arange(0, number_of_articles):
        
    # We need to ignore "live" pages since they are not articles
    if "live" in dailymail_news[n].find('a')['href']:  
        continue
    
    # Getting the link of the article
    link_d = dailymail_news[n].find('a')['href']
    list_links_d.append(link_d)
    
    # Getting the title
    title_d = dailymail_news[n].find('a').get_text()
    list_titles_d.append(title_d)
    
    # Creating unique ID
    NewsId_d = uuid.uuid1()
    if len(list_newsid_d) <= len(list_titles_d):
        list_newsid_d.append(NewsId_d)
    else:
        stop()
    
    # Getting the date and time
    now = datetime.now()
    dateNews = now.strftime("%d/%m/%Y, %H:%M:%S")
    if len(list_dates_d) <= len(list_titles_d):
        list_dates_d.append(dateNews)
    else:
        stop()
        
    # Getting website's name
    website_d = 'DailyMail'
    if len(list_websites_d) <= len(list_titles_d):
        list_websites_d.append(website_d)
    else:
        stop()


# df_show_info

df_show_dailymail = pd.DataFrame(
    {'Article Title': list_titles_d,
     'Article Link': list_links_d,
     'News ID': list_newsid_d,
     'Date': list_dates_d,
     'Website': list_websites_d
    })


df_show_dailymail


# url definition for The Star

url = "https://www.thestar.com.my/news/latest"
r2 = requests.get(url)
r2.status_code

# Save the cover page content as star
starpage = r2.content


# Parsing HTML content
page_soup = BeautifulSoup(starpage, 'html.parser')

# News identification
star_news = page_soup.find_all(class_="timeline-content")
print('Number of news article: {}' .format(len(starpage)))


# First, we'll define the number of articles we want:

number_of_articles = len(star_news)


# Create lists for news content, links and titles
list_links_s = []
list_titles_s = []
list_newsid_s = []
list_dates_s = []
list_websites_s = []

for n in np.arange(0, number_of_articles):
        
    # We need to ignore "live" pages since they are not articles
    if "live" in star_news[n].h2.find('a')['href']:  
        continue
        
    # Getting the link of the article
    link_s = star_news[n].h2.find('a')['href']
    list_links_s.append(link_s)
    
    # Getting the title
    title_s = star_news[n].h2.find('a').get_text()
    list_titles_s.append(title_s)
    
    # Creating unique ID
    NewsId = uuid.uuid1()
    list_newsid_s.append(NewsId)
    
    # Getting the date and time
    now = datetime.now()
    dateNews = now.strftime("%d/%m/%Y, %H:%M:%S")
    if len(list_dates_s) <= len(list_titles_s):
        list_dates_s.append(dateNews)
    else:
        stop()
        
    # Getting website's name
    website = 'The Star'
    if len(list_websites_s) <= len(list_titles_s):
        list_websites_s.append(website)
    else:
        stop()


# df_show_info

df_show_star = pd.DataFrame(
    {'Article Title': list_titles_s,
     'Article Link': list_links_s,
     'News ID': list_newsid_s,
     'Date': list_dates_s,
     'Website':list_websites_s
    })


df_show_star


# ### Export dataframe to csv file

import csv

df_allnews = pd.concat([df_show_guardian, df_show_dailymail, df_show_star], axis=0)  # axis=0 tells pandas to stack the second DataFrame UNDER the first one
df_allnews.to_csv('Crude Oil News Title and Link - All News.csv',mode = 'w', 
                    index=False, header=True)


