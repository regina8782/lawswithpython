import bs4
import requests
import re

url = "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001"
try:
    civil_url = requests.get(url)
except:
    print(requests.exceptions)
civil_obj = bs4.BeautifulSoup(civil_url.text, 'html.parser')

civil_article = civil_obj.select('div.law-reg-content div.row')
for article in civil_article:
    no = article.select('div.col-no')
    con = article.select('div.col-data.text-pre')
    print(no[0].text)
    print(con[0].text)