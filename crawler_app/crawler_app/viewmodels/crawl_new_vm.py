from crawler_app.viewmodels.base_viewmodel import ViewModelBase


class NewCrawl(ViewModelBase):
    def __init__(self):
        self.url = None
        self.depth = None
        self.keyword = None
        self.search_type = None
        self.previous_searches = [{'id': '12345', 'url': 'www.google.com'}, {'id': '12346', 'url': 'www.yahoo.com'}] 
        self.search_id = None

    def from_dict(self, data_dict):
        self.url = data_dict.get('url')
        self.depth = data_dict.get('depth')
        self.keyword = data_dict.get('keyword')
        self.search_type = data_dict.get('search_type')
        self.previous_searches = data_dict.get('previous_searches')
        self.search_id = data_dict.get('search_id')