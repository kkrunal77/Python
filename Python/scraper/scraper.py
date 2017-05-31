
# coding: utf-8

# In[ ]:




# In[1]:

from selenium import webdriver
import time
import re

driver = webdriver.Chrome("C:/Users/krunal/Anaconda3/selenium/webdriver/firefox/chromedriver.exe")

driver.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G")

time.sleep(5)
htmlSource = driver.page_source

import bs4
soup = bs4.BeautifulSoup(htmlSource)
table = soup.find("table", attrs={"id":"topGainers"})
headings = [th.get_text() for th in table.find("tr").find_all("th")]

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = [td.get_text() for td in row.find_all("td")]
    datasets.append(dataset)
print( datasets)


# In[21]:





import pandas as pd
df = pd.DataFrame(datasets)
df.columns = headings
df

###########################################USING REGEX###################################################
while True:

    driver.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G")
    time.sleep(5)
    htmlSource = driver.page_source
    x = re.findall(r"\<th title=\"(.*)" ,htmlSource,re.I)
    l = []
    for y in x:
    #     y = re.search(r"\<th title=\"(.*)", htmlSource, re.I)
        y= re.sub(r"\%\s", "",y)
        y = re.search(r'(.*)\"', y, re.I)  
        l.append(y.group(1))
    x1 = re.findall(r"\<td\>(.*)",htmlSource,re.I)
    y = re.sub(r"<[^>]+>", " ", str(x1))
    y = re.sub(r"(\s-\s)*(\s)", " ", str(y))
    y = re.sub(r"(\s-\s)|(\[\'\s)|\-\s\s\s|\-\s|\'\]|\'\,\s\'","",str(y))
    y = y.split()
    print(l[0:10])
    j=0
    for i in range(10,100,10):
        print(y[j:i])
        j = i
    	break
    time.sleep(60)
#     print(l[0:10])
#     print(y[0:10])
#     print(y[10:20])
#     print(y[20:30])
#     print(y[30:40])
#     print(y[40:50])
#     print(y[50:60])
#     print(y[60:70])
#     print(y[70:80])
#     print(y[80:90])
#     print(y[90:100])
#     time.sleep(60)

# In[ ]:




# In[ ]:
###########################################USING BS4###################################################
import re
import bs4
import time
import pandas as pd
from selenium import webdriver

global driver
driver = webdriver.Chrome("C:/Users/krunal/Anaconda3/selenium/webdriver/firefox/chromedriver.exe")

def job_function():
    driver.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G")
    time.sleep(5)
    htmlSource = driver.page_source
    soup = bs4.BeautifulSoup(htmlSource)
    table = soup.find("table", attrs={"id":"topGainers"})
    headings = [th.get_text() for th in table.find("tr").find_all("th")]
    datasets = []
    for row in table.find_all("tr")[1:]:
        dataset = [td.get_text() for td in row.find_all("td")]
        datasets.append(dataset)
    df = pd.DataFrame(datasets)
    df.columns = headings
    return df

while True:
    print(job_function())
    time.sleep(60)
##########################################################################################################
# In[27]:


import time


# In[ ]:

driver = webdriver.Chrome("C:/Users/krunal/Anaconda3/selenium/webdriver/firefox/chromedriver.exe")
driver.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G")
time.sleep(5)
htmlSource = driver.page_source


# In[ ]:

soup = bs4.BeautifulSoup(htmlSource)
table = soup.find("table", attrs={"id":"topGainers"})
headings = [th.get_text() for th in table.find("tr").find_all("th")]
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = [td.get_text() for td in row.find_all("td")]
    datasets.append(dataset)


# In[ ]:

df = pd.DataFrame(datasets)
df.columns = headings
df

