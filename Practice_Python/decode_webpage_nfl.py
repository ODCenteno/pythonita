"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage. https://www.nytimes.com/
"""

from bs4 import BeautifulSoup
import requests


def scrapping():
    url = 'https://www.nfl.com/teams/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, features="html.parser")

    # print(f'\n\n{"*"* 100}\n\n ')
    # for i in soup.find_all('p', {'class' : "d3-o-media-object__roofline nfl-c-custom-promo__headline"}):
    #     print(i.string)
    # print(f'\n\n{"*"* 100}\n\n ')
    # # for i in soup.find_all('h3'):   
    # #     print(i.string)

    for teams in soup.find_all(class_="d3-o-media-object__roofline nfl-c-custom-promo__headline"): 
        if teams.p: 
            print(teams.p.text.replace("\n", " ").strip())
        else: 
            print(teams.contents[0].strip())
if __name__ == '__main__':
    scrapping()