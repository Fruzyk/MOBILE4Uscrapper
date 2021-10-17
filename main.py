import requests
import re
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://fruzyk:Stefan306@cluster0.o651q.mongodb.net/Mobile4UScrapperDB?retryWrites=true&w=majority")
db = cluster["Mobile4UScrapperDB"]
collections = db["PhonesDB"]

URL = "https://mobile4ugsm.pl/pl/new/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("div", class_="product s-grid-3 product-main-wrap")
numberpgesprep = soup.find("ul", class_="paginator")
z = max([s for s in re.findall('[0-9,]', numberpgesprep.text.strip())])

for i in range(int(z)):
    URL = "https://mobile4ugsm.pl/pl/new/" + str(i+1)
    url_4links = "https://mobile4ugsm.pl"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("div", class_="product s-grid-3 product-main-wrap")
    fin_object = {}
    for index, job_element in enumerate(job_elements):
        name_element = job_element.find("span", class_="productname")
        price_element = job_element.find("div", class_="price")
        link_element = job_element.find("a", class_= "prodname")
        name = name_element.text.strip()
        price = price_element.text.strip()
        p = "".join([s for s in re.findall('[0-9,]', price)])
        link = url_4links + link_element.get('href')
        fin_object = {"URL": link, "name": name, "price": p + "zł"}
        collections.insert_one(fin_object)


