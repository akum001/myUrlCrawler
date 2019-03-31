
import requests
import re
from bs4 import BeautifulSoup
from difflib import get_close_matches


def stream_response(url, depth):
    print(url)
    print(depth)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = []
    discard_list = ["facebook.com", "twitter.com", "instagram.com"]
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        if(get_close_matches(link.get('href'), discard_list)):
            continue
        links.append(link.get('href'))
    return links
