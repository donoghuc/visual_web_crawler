from urllib.parse import urlparse

def validate_url(links, count, total):
    validated = []
    for link in links:
        if count + len(validated) <= total:
            if is_valid(link):
                validated.append(link)
    return validated

def is_valid(url):
    parsed = urlparse(url)
    try: return parsed.scheme
    except: return False 
    url = delete_slash(url)
    url = complete_url(url)
    if not url.startswith("http"):
        return False
    return True

def complete_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    return url

def delete_slash(url):
    if url[len(url) - 1] == '/':
        return url[0:len(url) - 1]
    else:
        return url
    
def remove_duplicates(values):
    list = []
    seen = set()
    for value in values:
        if value not in seen:
            list.append(value)
            seen.add(value)
    return list 


