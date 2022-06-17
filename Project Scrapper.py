from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    tdTags = tr.find_all('td')
    for tdTag in tdTags:
        row = tdTag.text.rstrip()
        temp_list.append(row)

starNames = []
distance =[]
mass = []
radius =[]
luminesence = []

for i in range(1,len(temp_list)):
    starNames.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminesence.append(temp_list[i][7])

headers = ['name','distance','mass','radius','luminosity']    
df2 = pd.DataFrame(list(zip(starNames,distance,mass,radius,luminesence)),columns=headers)
print(df2)

df2.to_csv('brightestStars.csv', index=True, index_label="id")
