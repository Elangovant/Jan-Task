
#Task 1
import pandas as pd
import numpy as np
data=np.genfromtxt('Data/Iris_data_sample.csv')
print(data)

#Task 2
data_1=pd.DataFrame.copy(data)
print(data_1["Species"])
print(data.loc[1,:])

#Task 3
x1=np.random.rand(5)
x2=np.random.rand(5)
d1=pd.DataFrame({'x':['a','b','c','d','e'], 'y':[1,2,3,4,5],'z':x1, 'w':x2})
d1.to_csv('test.csv')
print(d1)

#Task 4
import json
dictionary = {
    "id": ("04","05"),
    "name": ("Gokul", "Elango"),
    "depatment": ("Elc", "Mech")
}
with open("test.json",'w') as fp:
    json_object = json.dump(dictionary,fp)
print(json_object)


#Task-6  Copy the local files from one location to another
import shutil
shutil.copytree('D:\E-Books','D:\B')
print('Task Completed')

#Task-9 Scrap (Crawl) the particular product values in amazon.com and store
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://www.amazon.in/s?k=college+bags+for+men&crid=1IZN1PJEZ9IID&sprefix=college%2Caps%2C1539&ref=nb_sb_ss_ts-a-p_3_7')
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
cards=soup.find_all('div',{'data-asin':True,'data-component-type':'s-search-result'})
def scrape(card):
    title = card.h2.text.strip()
    # url=cards.h2.a.get('href')
    price = card.find('span', {'class': 'a-price-whole'}).text
    # print(title + ':', price)
    product = {'Title': title, 'Price': price}
    return product
ad_data=[]
for card in cards:
    product=scrape(card)
    ad_data.append(product)
with open('Scrape.csv','a') as f:
    field = ['Title', 'Price']
    writer = csv.DictWriter(f, fieldnames=field)
    for a in ad_data:
        writer.writerow(a)

# Task-10 Automate the Login by selenium module
from selenium import webdriver

driver=webdriver.Chrome('chromedriver.exe')
driver.get("https://demo.testfire.net/login.jsp")
a=driver.find_element_by_id("uid")
a.send_keys("Admin")
b=driver.find_element_by_id("passw")
b.send_keys("Admin")
driver.find_element_by_name("btnSubmit").click()
