import requests
from bs4 import BeautifulSoup

def scrape_data(url, selector):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.select_one(selector)
        return element.text if element else "Veri bulunamadı"
    except Exception as e:
        return str(e)