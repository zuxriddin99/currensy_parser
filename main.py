import requests
from bs4 import BeautifulSoup


def get_currencies():
    url = 'https://developers.google.com/google-ads/api/data/codes-formats#expandable-18'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    table = soup.find(id="currency_codes").findChild('table')
    head = table.tr
    elements = head.find_next_siblings()
    json_keys = [th.text for th in head.find_all('th')]
    resp = []
    for i in elements:
        values = [j.get_text() for j in i.find_all('td')]
        resp.append(dict(zip(json_keys, values)))

    return resp
