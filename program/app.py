import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = 'https://www.transfermarkt.com.br/spieler-statistik/wertvollstemannschaften/marktwertetop'
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

teams = pageSoup.find_all("td", {'class' : "no-border-links hauptlink"})
values = pageSoup.find_all("td", {'class': "rechts"})

team_list = []
value_list = []
 
for i in range(0, 25):
    team_list.append(teams[i].text)
    value_list.append(values[i].text)

df = pd.DataFrame({"Teams": team_list, "Values": value_list})
df.to_csv('most-valuable-clubs.csv')