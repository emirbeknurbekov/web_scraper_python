
import requests
from bs4 import BeautifulSoup

def get_news_titles(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    news_captions = soup.find_all('h6', class_='caption')

    return [caption.text for caption in news_captions]

url = 'http://alatoo.edu.kg/#gsc.tab=0'

news_titles = get_news_titles(url)

for index, title in enumerate(news_titles, start=1):
    print(f'{index}. {title}')
