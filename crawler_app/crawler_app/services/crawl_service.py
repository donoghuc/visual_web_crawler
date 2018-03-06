from crawler_app.services.spider import Spider
# from crawler_app.services.history_service import HistoryService
# from crawler_app.viewmodels.signin_viewmodel import SigninViewModel
# import crawler_app.infrastructure.cookie_auth as cookie_auth

from crawler_app.services.history_service import HistoryService
from crawler_app.services.helpers import build_json_graph
import pandas as pd
import json
import os

class CrawlService:
    @staticmethod
    def kick_off_crawl(userid, url, search_type, search_limit, keyword):
        '''start off a crawl'''
        if keyword:
            crawl_obj = Spider(url, search_type, search_limit, keyword)
        else:
            crawl_obj = Spider(url, search_type, search_limit)
        
        new_entry = HistoryService.add_history(userid, url, search_type, search_limit, keyword)
        build_frame = dict(node_id=[],node_depth=[],parent_node=[],domain=[],url=[],found=[])
        for i in crawl_obj.graph.nodes:
            build_frame['node_id'].append(i.id)
            build_frame['node_depth'].append(i.node_depth)
            build_frame['parent_node'].append(i.parent_node)
            build_frame['domain'].append(i.domain)
            build_frame['url'].append(i.url)
            build_frame['found'].append(str(i.found).lower())
            # print(i.found)
            
        df = pd.DataFrame(build_frame)
        df['lookup_id'] = new_entry

        print(HistoryService.add_data(df))

        return json.dumps(build_json_graph(df))