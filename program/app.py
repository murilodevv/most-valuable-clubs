import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = 'https://www.transfermarkt.com.br/spieler-statistik/wertvollstemannschaften/marktwertetop'
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

teams = pageSoup.find_all("td", {'class' : "no-border-links hauptlink"})
team_list = [i.text for i in teams]

values = pageSoup.find_all("td", {'class': "rechts"})
value_list = {i.text for i in values}

dict = {}

for i in teams:
    dict = {'team': i.text, 'value': '0'}
    print(dict)