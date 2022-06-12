from bs4 import BeautifulSoup
from selenium import webdriver
#import requests
import csv
import time
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
headers = ["name", "distance", "mass", "radius"]
star_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
"""table1=soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"})
tbody=table1.find_all("tbody")"""

def scrape():
    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            #print(index,td_tag)
            if index == 1:
                print(td_tag.find_all("a").contents)
                #temp_list.append(td_tag.find_all("a"))
            elif index== 3:
                #print(td_tag.contents)
                temp_list.append(td_tag.contents)
            elif index== 5:
                #print(td_tag.contents)
                temp_list.append(td_tag.contents)
            elif index== 6:
                #print(td_tag.contents)
                temp_list.append(td_tag.contents)
            else:
                temp_list.append("")
        #print(temp_list)
        """with open("scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)"""
scrape()