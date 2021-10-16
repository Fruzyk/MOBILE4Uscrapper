import requests
import json
from bs4 import BeautifulSoup


def write_json(new_data, filename='db.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        if new_data not in file_data['phones']:
            file_data['phones'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        else:
            return "Nothing changed"


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
    price = price_element.text
    link = url_4links + link_element.get('href')
    json_object = {
        "id": index+1,
        "url": link,
        "name": name,
        "price": price
        }
    write_json(json_object)



