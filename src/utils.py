import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from bs4 import BeautifulSoup as bs
from config import NEWS_URL, CATALOG_URL, ADVICE_URL, titles

def get_news():
    session = requests.Session()
    retry = Retry(connect = 3, backoff_factor = 0.5)
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('https://', adapter)
    response = session.get(NEWS_URL)
    soup = bs(response.text, 'lxml')
    names = soup.find_all('span', class_="rm-cm-item-text")
    links = soup.find_all('a', class_="item__link")
    for i in range(len(names)):
        names[i] = names[i].text
        while "  " in names[i] or "\n" in names[i]:
            names[i] = names[i].replace("  ", "")
            names[i] = names[i].replace("\n", "")
    for i in range(len(links)):
        links[i] = links[i]['href']
    data = list(zip(names, links))[0]
    return data

def get_catalog():
    session = requests.Session()
    retry = Retry(connect = 3, backoff_factor = 0.5)
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('https://', adapter)
    response = session.get(CATALOG_URL)
    soup = bs(response.text, 'lxml')
    catalog = soup.find_all('div', class_="indices__contents")
    blocks = catalog[0].find_all('div', class_="indices__tab-content")
    data = list()
    for i in range(len(blocks)):
        data.append(list())
        names = blocks[i].find_all('span', class_="indices__name")
        change = blocks[i].find_all('span',class_="indices__change")
        sum = blocks[i].find_all('span',class_="indices__sum")
        for j in range(len(names)):
            data[i].append([names[j].text, change[j].text, sum[j].text])
            while "  " in data[i][j][0] or "\n" in data[i][j][0]:
                data[i][j][0] = data[i][j][0].replace("  ", "")
                data[i][j][0] = data[i][j][0].replace("\n", "")
            while "  " in data[i][j][1] or "\n" in data[i][j][1]:
                data[i][j][1] = data[i][j][1].replace("  ", "")
                data[i][j][1] = data[i][j][1].replace("\n", "")
            while "  " in data[i][j][2] or "\n" in data[i][j][2]:
                data[i][j][2] = data[i][j][2].replace("  ", "")
                data[i][j][2] = data[i][j][2].replace("\n", "")
    return data

def get_catalog_text(id):
    catalog = get_catalog()
    text = titles[id] + "\n\n"
    for i in range(len(catalog[id])):
        item = catalog[id][i]
        text += "  *" + str(i + 1) + "*.  " + "  ".join(("*" + item[0] + "*", item[2], "(" + item[1] + ")")) + "\n\n"
    return text

def get_advice():
    session = requests.Session()
    retry = Retry(connect = 3, backoff_factor = 0.5)
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('https://', adapter)
    response = session.get(ADVICE_URL)
    soup = bs(response.text, 'lxml')
    titles = soup.find_all('span', class_="q-item__title")
    descriptions = soup.find_all('span', class_="q-item__description")
    links = soup.find_all('a', class_="q-item__link")
    for i in range(len(titles)):
        titles[i] = titles[i].text
        while "  " in titles[i] or "\n" in titles[i]:
            titles[i] = titles[i].replace("  ", "")
            titles[i] = titles[i].replace("\n", "")
    for i in range(len(descriptions)):
        descriptions[i] = descriptions[i].text
        while "  " in descriptions[i] or "\n" in descriptions[i]:
            descriptions[i] = descriptions[i].replace("  ", "")
            descriptions[i] = descriptions[i].replace("\n", "")
    for i in range(len(links)):
        links[i] = links[i]['href']
    data = list(zip(titles, descriptions, links))[0]
    return data