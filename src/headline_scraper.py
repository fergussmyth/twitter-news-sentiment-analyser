import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.co.uk/news'
response = requests.get(url)


def get_headlines():
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')




