import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.ca/DR-J-Projector-Projection-Compatible-activities/dp/B07174LM85/ref=sr_1_4?crid=3CSNGD89JVA2M&keywords=projector+mini&qid=1574039397&sprefix=projector%2Caps%2C420&sr=8-4"
headers1 = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
page = requests.get(URL, headers=headers1)
soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), "html.parser")
title = soup2.find(id="productTitle").get_text()
print(title.strip())
price =soup2.find(id="priceblock_ourprice").get_text()

convertedprice=float(price[4:9])
