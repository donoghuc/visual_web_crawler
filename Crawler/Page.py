import lxml.html
import requests
from collections import deque
from helpers import *

class Page(object):
    def __init__(self, url):
        #add http if only www
        self.url = complete(url)
        Page.to_visit = deque() # list of urls to crawl
        Page.visited_set = set()   # set of urls already crawled

        try:
            res = requests.get(self.url, headers = {'User-Agent': 'Mozilla/5.0'}, timeout=10)
            self.content = res.content
        except:
            print('failed request')

    def get_links(self, url):
        links_set = set()
        try:
            tree = lxml.html.fromstring(self.content)
        except:
            print('parser error')
            return links_set

        hrefs_list = tree.xpath('//a')
        for href in hrefs_list:
            link = href.get('href')
            if link is None:
                continue
            if self.havent_visited(link):
                links_set.add(link)

        return links_set
        
    def find_keyword(self, find_word):
        content = to_text(self.content)
        if find_word in content:
            return True
        return False
        
    def havent_visited(self, url):
        if url not in Page.visited_set and url not in Page.to_visit:
            return True
        else: return False