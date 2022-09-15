import requests
from bs4 import BeautifulSoup
import pprint

# Hacker News
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

def custom(links,subtext):
    hn = []
    for indx, item in enumerate(links):
        title = links[indx].getText()
        href = links[indx]. get('href', None)
        vote = subtext[indx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href , 'votes': points})
    return hn

pprint.pprint(custom(links,subtext))