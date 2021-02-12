"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage. https://www.nytimes.com/
"""

from bs4 import BeautifulSoup
import requests


def scrapping():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, features="html.parser")

    for i in soup.find_all('h2'):
        print(i.string)
    print(f'\n\n{"*"* 100}\n\n ')
    for i in soup.find_all('h3'):   
        print(i.string)


if __name__ == '__main__':
    scrapping()