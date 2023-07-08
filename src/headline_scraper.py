import requests
from bs4 import BeautifulSoup


def get_headlines():

    url = 'https://www.bbc.co.uk/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')




