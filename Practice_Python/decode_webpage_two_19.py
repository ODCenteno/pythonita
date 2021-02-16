"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file."""

import requests
from bs4 import BeautifulSoup

def scrapping():
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, features='html.parser')

    with open("nominsky2.txt", "w") as f:
        for paragraph in soup.find_all(dir="p"):
            f.write(paragraph.text.replace("em",""))

    nones = []
    try:
        for i in soup.find_all('p'):
            if i == 'em':
                i == ''
                nones.append('')
                continue
            else:
                text_file = open('moninsky.txt', 'w')
                n = text_file.write(i.string)
                text_file.close(n)
                print(i.string)
            print(f'\n\n{"*"* 100}\n\n ')
    except TypeError:
        print('I can handle it')


if __name__ == '__main__':
    scrapping()