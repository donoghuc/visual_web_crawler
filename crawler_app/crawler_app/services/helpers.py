import urllib.parse
from urllib.parse import urlparse
from urllib.request import urlopen
from lxml import html
from lxml.html.clean import Cleaner
import re
import pandas as pd
import json
import os

def validate_url(links, count, total):
    validated = []
    for link in links:
        if count + len(validated) <= total:
            if is_valid(link):
                validated.append(link)
    return validated

def is_valid(url):
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc and parsed.path:
        url = defrag_url(url)
        url = delete_slash(url)
        url = complete_url(url)
        if is_allowed(url):
            return True
    return False

def validate_seed(url):
    try:
        ret = urllib.request.urlopen(url)
        if ret.code == 200:
            return True
    except:
        return False 

def is_allowed(url):
    excluded_list = ['mailto:', 'tell:', '.css', '.js', 'favicon', '.jpg', '.jpeg', '.gif', '.pdf', '.doc']
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

def defrag_url(url):
    #return url with no fragment identifiers
    return urllib.parse.urldefrag(url)[0]
    
def remove_duplicates(values):
    list = []
    seen = set()
    for value in values:
        if value not in seen:
            list.append(value)
            seen.add(value)
    return list

# clean the document of the following unwanted tags
# to make searching for keyword easier:
cleaner = Cleaner(scripts=True,
                    style=True,
                    inline_style=True,
                    meta=True,
                    embedded=True,
                    comments=True,
                    frames=True,
                    forms=True)

def to_text(content):
    # clean the page
    cleaned = cleaner.clean_html(content)
    # get the text content
    result = html.fromstring(cleaned).text_content()
    # replace all the white spaces with a single space
    result = re.sub(r'/\s+/g', ' ', result).strip()
    return (result.lower())

def get_domain(url):
    return urlparse(url).netloc


def build_json_graph(df):
    '''build dictionary  to turn into JSON for D3 viz'''
    def make_graph(node_id, graph):
        '''recursively build a graph from nodes'''
        node = dict()
        if node_id in df['parent_node']:
            child_list = list()
            for idx,row in df.loc[df['parent_node'] == node_id].iterrows():
                if node_id != row['node_id']:
                    child_list.append(make_graph(row['node_id'],node))
            if len(child_list) > 0:
                node['children'] = child_list
            node['url'] = df.loc[df['node_id'] == node_id, 'url'].values[0]
            node['domain'] = df.loc[df['node_id'] == node_id, 'domain'].values[0]
            graph.update(node)
        return node

    graph = dict()
    make_graph(0,graph)
    start_node_children = [node for node in graph['children']]
    finalized_graph = dict(url=df.loc[df['node_id'] == 0, 'url'].values[0],
                            domain=df.loc[df['node_id'] == 0, 'domain'].values[0],
                            children=[node for node in graph['children']])
    return finalized_graph
