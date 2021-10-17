import requests
import re
from bs4 import BeautifulSoup


URL = "https://mobile4ugsm.pl/pl/new/"
url_4links = "https://mobile4ugsm.pl"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("div", class_="product s-grid-3 product-main-wrap")

for index, job_element in enumerate(job_elements):
    name_element = job_element.find("span", class_="productname")
    price_element = job_element.find("div", class_="price")
    link_element = job_element.find("a", class_= "prodname")
    name = name_element.text.strip()
    price = price_element.text.strip()
    p = "".join([s for s in re.findall('[0-9,]', price)])
    print(p)
    link = url_4links + link_element.get('href')
    fin_object = {
        'url': link,
        'name': name,
        'price': p + "zł"
        }
    print(fin_object)



