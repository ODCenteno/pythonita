"""
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
"""

import csv
import requests, bs4, pathlib


def scraping():

    url = 'https://www.nytimes.com/'
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    titles = []
    for i in soup.find_all('h2'):
        titles.append(i.string)
        #print(i.string)
    
    # print(titles)

    titles_txt = ' '.join([str(i) for i in titles])
    # for title in titles:
    #     titles_txt.join(title)
    
    print(f'\n\nEstos son los Titles_txt:\n\n{titles_txt}')


    # PERSISTIENDO = ['persistiendo.txt']

    with open('persistiendo.txt', mode = 'w') as f:
        f.write(titles_txt)

if __name__ == '__main__':
    scraping()
