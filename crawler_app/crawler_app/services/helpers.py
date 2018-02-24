from urllib.parse import urlparse
from lxml import html
from lxml.html.clean import Cleaner
import re

def validate_url(links, count, total):
    validated = []
    for link in links:
        if count + len(validated) <= total:
            if is_valid(link):
                validated.append(link)
    return validated

def is_valid(url):
    parsed = urlparse(url)
    if parsed.scheme:
        url = delete_slash(url)
        url = complete_url(url)
        if is_allowed(url)==True:
            return True
    return False

def is_allowed(url):
    excluded_list = ['mailto:', '.css', '.js', 'favicon', '.jpg', '.jpeg', '.gif', '.pdf', '.doc', '?', '#', 'tell:']
    if not any(word in url for word in excluded_list):
        return True
    return False

def complete_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    return url

def delete_slash(url):
    if url.startswith('//'):
        url = url[2:]
    return url
    
def remove_duplicates(values):
    list = []
    seen = set()
    for value in values:
        if value not in seen:
            list.append(value)
            seen.add(value)
    return list

cleaner = Cleaner(scripts=True,
                     style=True,
                     inline_style=True,
                     meta=True,
                     embedded=True,
                     comments=True)

def to_text(content):
    cleaned = cleaner.clean_html(content)
    text = html.fromstring(cleaned).text_content()
    text = re.sub(r'/\s+/g', ' ', text).strip()
    return text

def get_domain(url):
    return urlparse(url).netloc 
