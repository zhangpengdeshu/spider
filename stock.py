import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    try:
        html = requests.get(url)
        return html.text
    except:
        return None

def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find(id='quotesearch').find('ul').find_all('li')
    for item in items:
        yield{
              "code": item.find('a').get_text(),
              "link": item.find('a').get('href')
            }


def main():
    url = 'http://quote.eastmoney.com/stocklist.html'
    for item in parse_html(get_html(url)):
        print(item)


if __name__ == '__main__':
    main()
