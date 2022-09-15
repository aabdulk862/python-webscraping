import requests
from bs4 import BeautifulSoup
import pprint

# Hacker News
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink')
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext +  subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def custom(links,subtext):
    hn = []
    for indx, item in enumerate(links):
        title = links[indx].getText()
        href = links[indx]. get('href', None)
        vote = subtext[indx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href , 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(custom(mega_links,mega_subtext))